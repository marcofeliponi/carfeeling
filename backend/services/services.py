from firebase_admin import firestore, initialize_app
from firebase_admin import firestore

initialize_app()
db = firestore.client()

def get_cars_service():
    try:
        cars = db.collection("cars").get()

        if not cars:
            return {"error": "No cars found"}
        
        return {
            "cars": [car.to_dict() for car in cars]
        }

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}