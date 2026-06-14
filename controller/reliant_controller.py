"""
Controller לסומך (Reliant)
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from dto.reliant_dto import ReliantCreateDTO, ReliantResponseDTO
from repository.reliant_repository import ReliantRepository


router = APIRouter(prefix="/reliants", tags=["Reliant"])


@router.get("/", response_model=List[ReliantResponseDTO])
def get_all(db: Session = Depends(get_db)):
    """שליפת כל רשומות הסומך"""
    return ReliantRepository(db).get_all()


@router.get("/{reliant_id}", response_model=ReliantResponseDTO)
def get_one(reliant_id: int, db: Session = Depends(get_db)):
    """שליפת סומך לפי מזהה"""
    item = ReliantRepository(db).get_by_id(reliant_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"סומך {reliant_id} לא נמצא")
    return item


@router.post("/", response_model=ReliantResponseDTO, status_code=201)
def create(data: ReliantCreateDTO, db: Session = Depends(get_db)):
    """יצירת רשומת סומך חדשה"""
    return ReliantRepository(db).create(data)


@router.put("/{reliant_id}", response_model=ReliantResponseDTO)
def update(reliant_id: int, data: ReliantCreateDTO, db: Session = Depends(get_db)):
    """עדכון רשומת סומך"""
    updated = ReliantRepository(db).update(reliant_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"סומך {reliant_id} לא נמצא")
    return updated


@router.delete("/{reliant_id}", status_code=204)
def delete(reliant_id: int, db: Session = Depends(get_db)):
    """מחיקת רשומת סומך"""
    if not ReliantRepository(db).delete(reliant_id):
        raise HTTPException(status_code=404, detail=f"סומך {reliant_id} לא נמצא")
    return None
