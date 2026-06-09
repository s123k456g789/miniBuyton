"""
מודל לטבלת Customers (לקוחות)
מייצג לקוח שצריך כמות מועטת של בטון
"""

from sqlalchemy import Column, Integer, String   # סוגי עמודות
from database import Base                        # מחלקת בסיס למודלים


class Customer(Base):
    """
    מחלקת מודל ללקוח
    הטבלה ב-DB: Customers
    תפקיד: לקוחות שמזמינים בטון בכמות קטנה
    """

    __tablename__ = "Customers"   # שם הטבלה כפי שהוגדרה ב-SQL

    # מפתח ראשי - מתחיל מ-100 ועולה ב-1 בכל הוספה
    id = Column(Integer, primary_key=True, autoincrement=True)

    # שם פרטי הלקוח (עד 15 תווים)
    first_name = Column(String(15), nullable=True)

    # שם  משפחה הלקוח (עד 15 תווים)
    last_name = Column(String(15), nullable=True)

    # שם  משתמש של הלקוח (עד 15 תווים)
    user_name = Column(String(15), nullable=True)

    # סיסמא של הלקוח (עד 15 תווים)
    password = Column(String(15), nullable=True)


    # מספר טלפון של הלקוח (עד 20 תווים)
    phone = Column(String(20), nullable=True)
