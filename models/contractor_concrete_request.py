"""
מודל לטבלת ContractorConcreteRequests (הצעות של קבלנים)
מייצג הצעה של קבלן עם שאריות בטון
"""

from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey  # סוגי עמודות
from database import Base
# מחלקת בסיס למודלים


class ContractorConcreteRequest(Base):
    """
    מחלקת מודל להצעת קבלן עם שאריות בטון
    הטבלה ב-DB: ContractorConcreteRequests
    תפקיד: שמירת הצעות של קבלנים עם שאריות בטון שיש להם
    """

    __tablename__ = "ContractorConcreteRequests"

    # מפתח ראשי - מתחיל מ-600 ועולה ב-1
    request_id = Column(Integer, primary_key=True, autoincrement=True)

    # מזהה סוג הבטון - מפתח זר לטבלת Concrete_type
    concrete_id = Column(Integer, ForeignKey("Concrete_type.id"), nullable=True)

    # מזהה הקבלן - מפתח זר לטבלת Contractors
    contractor_id = Column(Integer, ForeignKey("Contractors.id"), nullable=True)

    # כמות הבטון שנשארה לקבלן במטרים מעוקבים
    quantity = Column(DECIMAL(6, 2), nullable=True)

    # כתובת הקבלן / מקום ההצעה
    address = Column(String(255), nullable=True)

    # קו רוחב לאיתור על המפה
    lat = Column(DECIMAL(9, 6), nullable=True)

    # קו אורך לאיתור על המפה
    lng = Column(DECIMAL(9, 6), nullable=True)

    # זמן תפוגה של ההצעה (בטון נשארות חיים זמן קצר)
    expiry_time = Column(DateTime, nullable=True)

    # אזור גיאוגרפי (לסינון מהיר לפי אזורים)
    region = Column(String(100), nullable=True)

    # מחיר (לאישןר הלקוח)
    price = Column(String(100), nullable=True)

