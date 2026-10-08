from fastapi import FastAPI
from src.predict import predict_churn
from src.schemas import CustomerData

app = FastAPI(
    title="Telco Customer Churn API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Telco Customer Churn Prediction API"
    }

@app.post("/predict")
def predict(customer: CustomerData):
    customer_data = customer.model_dump()

    return predict_churn(customer_data)