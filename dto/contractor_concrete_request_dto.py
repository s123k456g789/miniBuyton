"""
DTO להצעת בטון של קבלן (ContractorConcreteRequest)
"""

from typing import Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field


class ContractorConcreteRequestCreateDTO(BaseModel):
    """
    DTO ליצירת הצעת בטון חדשה מקבלן
    """

    # מזהה סוג הבטון
    concrete_id: Optional[int] = Field(None, description="מזהה סוג הבטון")

    # מזהה הקבלן שמציע
    contractor_id: Optional[int] = Field(None, description="מזהה הקבלן")

    # כמות הבטון שיש לקבלן
    quantity: Optional[Decimal] = Field(None, description="כמות בטון שנותרה")

    # כתובת היכן הבטון נמצא
    address: Optional[str] = Field(None, max_length=255, description="כתובת הקבלן")

    # קו רוחב
    lat: Optional[Decimal] = Field(None, description="קו רוחב")

    # קו אורך
    lng: Optional[Decimal] = Field(None, description="קו אורך")

    # זמן תפוגה של ההצעה
    expiry_time: Optional[datetime] = Field(None, description="זמן תפוגת ההצעה")

    # אזור
    region: Optional[str] = Field(None, max_length=100, description="אזור גיאוגרפי")


class ContractorConcreteRequestResponseDTO(BaseModel):
    """
    DTO להחזרת הצעת קבלן מהשרת
    """

    request_id: int
    concrete_id: Optional[int] = None
    contractor_id: Optional[int] = None
    quantity: Optional[Decimal] = None
    address: Optional[str] = None
    lat: Optional[Decimal] = None
    lng: Optional[Decimal] = None
    expiry_time: Optional[datetime] = None
    region: Optional[str] = None

    class Config:
        from_attributes = True
