"""
DTO לבקשת בטון של לקוח (ConcreteRequest)
"""

from typing import Optional
from datetime import date as DateType
from decimal import Decimal
from pydantic import BaseModel, Field


class ConcreteRequestCreateDTO(BaseModel):
    """
    DTO ליצירת בקשת בטון חדשה מלקוח
    """

    # מזהה הלקוח שמבקש את הבטון
    customer_id: Optional[int] = Field(None, description="מזהה הלקוח")

    # מזהה המטרה / קטגוריה
    purpose_id: Optional[int] = Field(None, description="מזהה המטרה")

    # כמות הבטון הרצויה (במ"ק)
    quantity: Optional[Decimal] = Field(None, description="כמות בטון במ\"ק")

    # הכתובת לאספקה
    address: Optional[str] = Field(None, max_length=255, description="כתובת אספקה")

    # קו רוחב גיאוגרפי (חובה)
    lat: Decimal = Field(..., description="קו רוחב")

    # קו אורך גיאוגרפי (חובה)
    lng: Decimal = Field(..., description="קו אורך")

    # אזור (אופציונלי)
    region: Optional[str] = Field(None, max_length=100, description="אזור גיאוגרפי")


class ConcreteRequestResponseDTO(BaseModel):
    """
    DTO להחזרת בקשת בטון מהשרת
    כולל את כל השדות + מזהה ותאריך
    """

    request_id: int                       # מזהה הבקשה שנוצר ב-DB
    customer_id: Optional[int] = None
    purpose_id: Optional[int] = None
    quantity: Optional[Decimal] = None
    address: Optional[str] = None
    lat: Decimal
    lng: Decimal
    date: DateType                        # תאריך הבקשה
    region: Optional[str] = None

    class Config:
        from_attributes = True
