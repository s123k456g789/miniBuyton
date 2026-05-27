"""
DTO למטרה / קטגוריה (Purpose)
"""

from typing import Optional
from pydantic import BaseModel, Field


class PurposeCreateDTO(BaseModel):
    """DTO ליצירת רשומת מטרה חדשה"""

    Purpose: Optional[str] = Field(None, max_length=50, description="תיאור המטרה")


class PurposeResponseDTO(BaseModel):
    """DTO להחזרת רשומת מטרה"""

    id: int
    Purpose: Optional[str] = None

    class Config:
        from_attributes = True
