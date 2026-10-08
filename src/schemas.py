from typing import Literal
from pydantic import BaseModel, Field

class CustomerData(BaseModel):
    senior_citizen: Literal["Yes", "No"]
    partner: Literal["Yes", "No"]
    dependents: Literal["Yes", "No"]

    tenure_months: int = Field(ge=0)

    internet_service: Literal[
        "DSL",
        "Fiber optic",
        "No"
    ]

    online_security: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    online_backup: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    device_protection: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    tech_support: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    streaming_tv: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    streaming_movies: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    contract: Literal[
        "Month-to-month",
        "One year",
        "Two year"
    ]

    paperless_billing: Literal["Yes", "No"]

    payment_method: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]

    monthly_charges: float = Field(ge=0)
    total_charges: float = Field(ge=0)