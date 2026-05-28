"""
שירות התאמה (Matching Service) - שלד עם פונקציות לדוגמא בלבד!
========================================================
לב הלוגיקה של הפרויקט: התאמה בין לקוחות (שצריכים כמות מועטה של בטון)
לבין קבלנים (שנשארו עם שאריות בטון).

הקובץ הזה מכיל פונקציות לדוגמא - דורש מימוש מלא בהמשך.
"""

from typing import List
from sqlalchemy.orm import Session
from models.concrete_request import ConcreteRequest
from models.contractor_concrete_request import ContractorConcreteRequest


class MatchingService:
    """
    שירות שמתאים בין בקשות לקוחות להצעות של קבלנים
    שלד בלבד - דורש מימוש מלא בהמשך
    """

    def __init__(self, db: Session):
        # שמירת סשן ה-DB לשימוש בפונקציות
        self.db = db

    def find_matches_for_customer(self, request_id: int) -> List[ContractorConcreteRequest]:
        """
        מציאת הצעות קבלנים שמתאימות לבקשת לקוח ספציפית
        TODO: למימוש בעתיד
        השלבים שצריך לבצע:
        1. לטעון את בקשת הלקוח לפי request_id
        2. לחשב את האזור והמיקום
        3. לחפש הצעות באותו אזור עם כמות מתאימה
        4. למיין לפי מרחק / מחיר / זמן תפוגה
        5. להחזיר רשימה מסודרת
        """
        # פונקציה לדוגמא - להחליף במימוש אמיתי בהמשך
        raise NotImplementedError("פונקציה זו עדיין לא ממומשת - יש להוסיף לוגיקת התאמה")

    def find_matches_for_contractor(self, offer_id: int) -> List[ConcreteRequest]:
        """
        מציאת לקוחות פוטנציאליים להצעה של קבלן
        TODO: למימוש בעתיד
        """
        raise NotImplementedError("פונקציה זו עדיין לא ממומשת")

    def calculate_distance(self, lat1: float, lng1: float, lat2: float, lng2: float) -> float:
        """
        חישוב מרחק בין שתי נקודות גיאוגרפיות
        TODO: לממש את נוסחת Haversine לחישוב מרחק על פני כדור הארץ
        """
        raise NotImplementedError("יש לממש חישוב מרחק (Haversine formula)")
