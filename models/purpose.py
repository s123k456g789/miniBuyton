"""
מודל לטבלת Purpose (מטרה / קטגוריה)
טבלת lookup למטרות שונות לשימוש בבטון
"""

from sqlalchemy import Column, Integer, String
from database import Base


class Purpose(Base):
    """
    מחלקת מודל למטרת שימוש בבטון
    הטבלה ב-DB: Purpose
    תפקיד: רשימת קטגוריות / מטרות לשימוש בבטון (יסודות, רצפה, גדר וכו')
    """

    __tablename__ = "Purpose"

    # מפתח ראשי - מתחיל מ-1400
    id = Column(Integer, primary_key=True, autoincrement=True)

    # תיאור המטרה (עד 50 תווים)
    # שם העמודה ב-DB: Purpose
    Purpose = Column("Purpose", String(50), nullable=True)
