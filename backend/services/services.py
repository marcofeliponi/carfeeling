from firebase_admin import firestore, initialize_app

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
            car_analysis = db.collection("car_analysis").where("car", "==", car).get()

        if not car_analysis:
            return {"error": f"No analysis found for {car}"}

        data = {
            "analysis": [analysis.to_dict() for analysis in car_analysis]
        }
        
        return data
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}