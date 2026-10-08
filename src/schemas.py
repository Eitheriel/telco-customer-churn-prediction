from pydantic import BaseModel


class CustomerData(BaseModel):
    senior_citizen: str
    partner: str
    dependents: str
    tenure_months: int
    internet_service: str
    online_security: str
    online_backup: str
    device_protection: str
    tech_support: str
    streaming_tv: str
    streaming_movies: str
    contract: str
    paperless_billing: str
    payment_method: str
    monthly_charges: float
    total_charges: float