"""
מודל לטבלת Contractors (קבלנים)
מייצג קבלן שנשארו לו שאריות בטון להציע
"""

from sqlalchemy import Column, Integer, String   # סוגי עמודות
from database import Base                        # מחלקת בסיס למודלים


class Contractor(Base):
    """
    מחלקת מודל לקבלן
    הטבלה ב-DB: Contractors
    תפקיד: קבלנים שיש להם שאריות בטון להציע ללקוחות
    """

    __tablename__ = "Contractors"   # שם הטבלה כפי שהוגדרה ב-SQL

    # מפתח ראשי - מתחיל מ-300 ועולה ב-1 בכל הוספה
    id = Column(Integer, primary_key=True, autoincrement=True)

    # שם הקבלן (עד 15 תווים)
    name = Column(String(15), nullable=True)

    # מספר טלפון של הקבלן (עד 15 תווים)
    phone = Column(String(15), nullable=True)
