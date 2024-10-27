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
    
def save_car_analysis(car, analysis):
    try:
        car_analysis = db.collection("car_analysis").where("car", "==", car).get()
        for doc in car_analysis:
            doc.reference.delete()
            
        db.collection("car_analysis").add({
            "car": car,
            "created_at": firestore.SERVER_TIMESTAMP,
            **analysis
        })
        
        return {"message": f"Analysis saved successfully for {car}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    