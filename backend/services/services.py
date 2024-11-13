import os
import json
from firebase_admin import firestore, initialize_app
import requests
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

initialize_app()
db = firestore.client()

def get_cars_service():
    try:
        cars = db.collection("cars").get()

        if not cars:
            return {"error": "No cars found"}
        
        data = {
            "cars": [car.to_dict() for car in cars]
        }

        return data

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def get_brands_service():
    try:
        brands = db.collection("brands").get()

        if not brands:
            return {"error": "No brands found"}
        
        data = {
            "brands": [brand.to_dict() for brand in brands]
        }

        return data

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def save_car_analysis(car, analysis, score, year):
    try:
        if year:
            car_analysis = db.collection("car_analysis").where("carAndYear", "==", f"{car}_{year}").get()
        else:
            car_analysis = db.collection("car_analysis").where("car", "==", car).get()

        for doc in car_analysis:
            doc.reference.delete()
            
        car_analysis_data = {
            "score": score,
            "created_at": firestore.SERVER_TIMESTAMP,
            **analysis
        }

        if year:
            car_analysis_data["carAndYear"] = f"{car}_{year}"
        else:
            car_analysis_data["car"] = car
        
        db.collection("car_analysis").add(car_analysis_data)
        
        return {"message": f"Analysis saved successfully for {car} {year if year else ''}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def get_car_analysis_service(car, query_params):
    try:
        car_analysis = []

        if query_params.get("year"):
            car_and_year = f'{car}_{query_params.get("year")}'
            car_analysis = db.collection("car_analysis").where("carAndYear", "==", car_and_year).get()

            if not car_analysis:
                return {"error": f"No analysis found for {car} {query_params.get('year')}"}
        else:
            car_analysis = db.collection("car_analysis").where("car", "==", car).get()

            if not car_analysis:
                start_at = f'{car}_'
                end_at = start_at + '\uf8ff'

                car_analysis = db.collection('car_analysis') \
                    .where('carAndYear', '>=', start_at) \
                    .where('carAndYear', '<=', end_at) \
                    .get()
                
                car_analysis = sorted(car_analysis, key=lambda x: x.to_dict()['created_at'], reverse=True)

        if not car_analysis:
            return {"error": f"No analysis found for {car}"}

        data = {
            "analysis": [analysis.to_dict() for analysis in car_analysis]
        }
        
        return data
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def get_car_comparison_service(car):
    try:
        compared_car = db.collection("cars").where("model", "==", car).get()

        if not compared_car:
            return {"error": f"{car} not found"}

        compared_car_price = compared_car[0].to_dict()["price"]
        lower_bound = compared_car_price - 10000
        upper_bound = compared_car_price + 10000
        
        comparison_cars = db.collection("cars").where("price", ">", lower_bound).where("price", "<", upper_bound).limit(3).get()
    
        if not comparison_cars:
            return {"error": f"No cars found to compare with {car}"}

        scores = []
        for car in comparison_cars:
            model = car.to_dict()["model"]
            price = car.to_dict()["price"]
            brand = car.to_dict()["brand"]
            year  = car.to_dict()["year"]

            score = db.collection("car_analysis").where("car", "==", model).get()

            if not score:
                scores.append({"model": model, "score": 0, "price": price, "brand": brand, "year": year})
            else:
                scores.append({"model": model, "score": score[0].to_dict()["score"], "price": price, "brand": brand, "year": year})

        data = {
            "scores": scores
        }
        
        return data
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def ai_chat_service(token, messages=None):
    try:   
        idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), os.environ.get("google-client-id"))

        if not idinfo["sub"]:
            return {"error": "Invalid token"}

        if not messages:
            return {"error": "Messages are required at this endpoint"}

        default_rule = {
            "role": "system",
            "content": "Você é um auxiliar do site Carfeeling em opiniões sobre o veículo informado pelo usuário, você pode apenas responder sobre este carro e de forma objetiva."
        }
        messages.insert(0, default_rule)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {_get_openapi_key()}",
        }
        data = {
            "model": "gpt-3.5-turbo-0125",
            "n": 1,
            "messages": messages
        }
    
        response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
        
        return response.json()
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def _get_openapi_key():
    secret = os.environ.get("openai-apikey")
    return secret