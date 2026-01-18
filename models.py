from pydantic import BaseModel

class CreditCard(BaseModel):
    number: str
    cvv: str
    expiry: str