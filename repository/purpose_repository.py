"""
Repository למטרה / קטגוריה (Purpose) - טבלת lookup
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from models.purpose import Purpose
from dto.purpose_dto import PurposeCreateDTO


class PurposeRepository:
    """מחלקת גישה לנתוני מטרות / קטגוריות"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Purpose]:
        """שליפת כל המטרות"""
        return self.db.query(Purpose).all()

    def get_by_id(self, purpose_id: int) -> Optional[Purpose]:
        """שליפת מטרה לפי מזהה"""
        return self.db.query(Purpose).filter(Purpose.id == purpose_id).first()

    def create(self, data: PurposeCreateDTO) -> Purpose:
        """יצירת מטרה חדשה"""
        new_item = Purpose(Purpose=data.Purpose)
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def update(self, purpose_id: int, data: PurposeCreateDTO) -> Optional[Purpose]:
        """עדכון מטרה"""
        existing = self.get_by_id(purpose_id)
        if not existing:
            return None
        if data.Purpose is not None:
            existing.Purpose = data.Purpose
        self.db.commit()
        self.db.refresh(existing)
        return existing

    def delete(self, purpose_id: int) -> bool:
        """מחיקת מטרה"""
        existing = self.get_by_id(purpose_id)
        if not existing:
            return False
        self.db.delete(existing)
        self.db.commit()
        return True
