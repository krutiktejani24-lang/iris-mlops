from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI(
    title="Iris Prediction API",
    description="Predict Iris Flower Species",
    version="1.0"
)

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {
        "message": "Welcome to Iris Prediction API 🚀"
    }

@app.post("/predict")
def predict(data: IrisInput):

    prediction = model.predict([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    species = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    return {
        "prediction": int(prediction[0]),
        "species": species[int(prediction[0])]
    }