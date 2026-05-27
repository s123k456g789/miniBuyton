"""
Repository לקבלנים (Contractor)
מטפל בכל הפעולות מול טבלת Contractors ב-DB
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from models.contractor import Contractor
from dto.contractor_dto import ContractorCreateDTO


class ContractorRepository:
    """מחלקת גישה לנתוני קבלנים"""

    def __init__(self, db: Session):
        # שמירת הסשן של DB לשימוש בפונקציות
        self.db = db

    def get_all(self) -> List[Contractor]:
        """שליפת כל הקבלנים"""
        return self.db.query(Contractor).all()

    def get_by_id(self, contractor_id: int) -> Optional[Contractor]:
        """שליפת קבלן לפי מזהה"""
        return self.db.query(Contractor).filter(Contractor.id == contractor_id).first()

    def create(self, contractor_data: ContractorCreateDTO) -> Contractor:
        """יצירת קבלן חדש"""
        new_contractor = Contractor(
            name=contractor_data.name,
            phone=contractor_data.phone
        )
        self.db.add(new_contractor)
        self.db.commit()
        self.db.refresh(new_contractor)
        return new_contractor

    def update(self, contractor_id: int, contractor_data: ContractorCreateDTO) -> Optional[Contractor]:
        """עדכון קבלן קיים"""
        existing = self.get_by_id(contractor_id)
        if not existing:
            return None

        if contractor_data.name is not None:
            existing.name = contractor_data.name
        if contractor_data.phone is not None:
            existing.phone = contractor_data.phone

        self.db.commit()
        self.db.refresh(existing)
        return existing

    def delete(self, contractor_id: int) -> bool:
        """מחיקת קבלן"""
        existing = self.get_by_id(contractor_id)
        if not existing:
            return False
        self.db.delete(existing)
        self.db.commit()
        return True
