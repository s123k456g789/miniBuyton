"""
Controller למטרה / קטגוריה (Purpose)
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from dto.purpose_dto import PurposeCreateDTO, PurposeResponseDTO
from repository.purpose_repository import PurposeRepository


router = APIRouter(prefix="/purposes", tags=["Purpose"])


@router.get("/", response_model=List[PurposeResponseDTO])
def get_all(db: Session = Depends(get_db)):
    """שליפת כל המטרות"""
    return PurposeRepository(db).get_all()


@router.get("/{purpose_id}", response_model=PurposeResponseDTO)
def get_one(purpose_id: int, db: Session = Depends(get_db)):
    """שליפת מטרה לפי מזהה"""
    item = PurposeRepository(db).get_by_id(purpose_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"מטרה {purpose_id} לא נמצאה")
    return item


@router.post("/", response_model=PurposeResponseDTO, status_code=201)
def create(data: PurposeCreateDTO, db: Session = Depends(get_db)):
    """יצירת מטרה חדשה"""
    return PurposeRepository(db).create(data)


@router.put("/{purpose_id}", response_model=PurposeResponseDTO)
def update(purpose_id: int, data: PurposeCreateDTO, db: Session = Depends(get_db)):
    """עדכון מטרה"""
    updated = PurposeRepository(db).update(purpose_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"מטרה {purpose_id} לא נמצאה")
    return updated


@router.delete("/{purpose_id}", status_code=204)
def delete(purpose_id: int, db: Session = Depends(get_db)):
    """מחיקת מטרה"""
    if not PurposeRepository(db).delete(purpose_id):
        raise HTTPException(status_code=404, detail=f"מטרה {purpose_id} לא נמצאה")
    return None
