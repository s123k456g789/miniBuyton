from pydantic import BaseModel

class ContractorRequestDto(BaseModel):
    lat: float
    lng: float
    concrete_id: int
    quantity: float