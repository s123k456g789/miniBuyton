"""
DTO לחוזק בטון (Strength)
"""

from typing import Optional
from pydantic import BaseModel, Field


class StrengthCreateDTO(BaseModel):
    """DTO ליצירת רשומת חוזק חדשה"""

    strength: Optional[str] = Field(None, max_length=50, description="תיאור החוזק")


class StrengthResponseDTO(BaseModel):
    """DTO להחזרת רשומת חוזק"""

    id: int
    strength: Optional[str] = None

    class Config:
        from_attributes = True
