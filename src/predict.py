import joblib
import pandas as pd
from src.config import MODEL_PATH, THRESHOLD, FEATURES

model = joblib.load(MODEL_PATH)

def prepare_customer_data(customer_data: dict) -> dict:
    return {
        "Senior Citizen": customer_data["senior_citizen"],
        "Partner": customer_data["partner"],
        "Dependents": customer_data["dependents"],
        "Tenure Months": customer_data["tenure_months"],
        "Internet Service": customer_data["internet_service"],
        "Online Security": customer_data["online_security"],
        "Online Backup": customer_data["online_backup"],
        "Device Protection": customer_data["device_protection"],
        "Tech Support": customer_data["tech_support"],
        "Streaming TV": customer_data["streaming_tv"],
        "Streaming Movies": customer_data["streaming_movies"],
        "Contract": customer_data["contract"],
        "Paperless Billing": customer_data["paperless_billing"],
        "Payment Method": customer_data["payment_method"],
        "Monthly Charges": customer_data["monthly_charges"],
        "Total Charges": customer_data["total_charges"]
    }

def predict_churn(customer_data: dict) -> dict:
    customer_data = prepare_customer_data(customer_data)

    df = pd.DataFrame([customer_data])
    df = df[FEATURES]

    probability = model.predict_proba(df)[:, 1][0]
    prediction = int(probability >= THRESHOLD)

    return {
        "churn_probability": float(probability),
        "prediction": prediction,
        "threshold": THRESHOLD
    }
