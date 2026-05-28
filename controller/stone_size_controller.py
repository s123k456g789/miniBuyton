"""
Controller לגודל אבן (StoneSize)
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from dto.stone_size_dto import StoneSizeCreateDTO, StoneSizeResponseDTO
from repository.stone_size_repository import StoneSizeRepository


router = APIRouter(prefix="/stone-sizes", tags=["Stone Size"])


@router.get("/", response_model=List[StoneSizeResponseDTO])
def get_all(db: Session = Depends(get_db)):
    """שליפת כל גדלי האבן"""
    return StoneSizeRepository(db).get_all()


@router.get("/{stone_size_id}", response_model=StoneSizeResponseDTO)
def get_one(stone_size_id: int, db: Session = Depends(get_db)):
    """שליפת גודל אבן לפי מזהה"""
    item = StoneSizeRepository(db).get_by_id(stone_size_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"גודל אבן {stone_size_id} לא נמצא")
    return item


@router.post("/", response_model=StoneSizeResponseDTO, status_code=201)
def create(data: StoneSizeCreateDTO, db: Session = Depends(get_db)):
    """יצירת רשומת גודל אבן חדשה"""
    return StoneSizeRepository(db).create(data)


@router.put("/{stone_size_id}", response_model=StoneSizeResponseDTO)
def update(stone_size_id: int, data: StoneSizeCreateDTO, db: Session = Depends(get_db)):
    """עדכון גודל אבן"""
    updated = StoneSizeRepository(db).update(stone_size_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"גודל אבן {stone_size_id} לא נמצא")
    return updated


@router.delete("/{stone_size_id}", status_code=204)
def delete(stone_size_id: int, db: Session = Depends(get_db)):
    """מחיקת רשומת גודל אבן"""
    if not StoneSizeRepository(db).delete(stone_size_id):
        raise HTTPException(status_code=404, detail=f"גודל אבן {stone_size_id} לא נמצא")
    return None
