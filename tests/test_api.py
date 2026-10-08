from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_predict_valid_customer():
    payload = {
        "senior_citizen": "No",
        "partner": "No",
        "dependents": "No",
        "tenure_months": 5,
        "internet_service": "Fiber optic",
        "online_security": "No",
        "online_backup": "No",
        "device_protection": "No",
        "tech_support": "No",
        "streaming_tv": "Yes",
        "streaming_movies": "Yes",
        "contract": "Month-to-month",
        "paperless_billing": "Yes",
        "payment_method": "Electronic check",
        "monthly_charges": 89.5,
        "total_charges": 420.3
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200
    data = response.json()
    assert "churn_probability" in data
    assert "prediction" in data
    assert "threshold" in data



def test_predict_invalid_contract():
    payload = {
        "senior_citizen": "No",
        "partner": "No",
        "dependents": "No",
        "tenure_months": 5,
        "internet_service": "Fiber optic",
        "online_security": "No",
        "online_backup": "No",
        "device_protection": "No",
        "tech_support": "No",
        "streaming_tv": "Yes",
        "streaming_movies": "Yes",
        "contract": "Random contract",
        "paperless_billing": "Yes",
        "payment_method": "Electronic check",
        "monthly_charges": 89.5,
        "total_charges": 420.3
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422