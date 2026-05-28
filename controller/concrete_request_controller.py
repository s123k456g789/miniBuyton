"""
Controller לבקשות בטון של לקוחות (ConcreteRequest)
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from dto.concrete_request_dto import ConcreteRequestCreateDTO, ConcreteRequestResponseDTO
from repository.concrete_request_repository import ConcreteRequestRepository


router = APIRouter(prefix="/concrete-requests", tags=["Concrete Requests"])


@router.get("/", response_model=List[ConcreteRequestResponseDTO])
def get_all_requests(
    # פרמטר אופציונלי - לסנן לפי אזור
    region: str = Query(None, description="סינון לפי אזור"),
    db: Session = Depends(get_db)
):
    """
    שליפת בקשות בטון של לקוחות
    GET /concrete-requests/
    אפשר להעביר ?region=צפון לסינון לפי אזור
    """
    repo = ConcreteRequestRepository(db)
    if region:
        return repo.get_by_region(region)
    return repo.get_all()


@router.get("/{request_id}", response_model=ConcreteRequestResponseDTO)
def get_request(request_id: int, db: Session = Depends(get_db)):
    """שליפת בקשה ספציפית לפי מזהה"""
    req = ConcreteRequestRepository(db).get_by_id(request_id)
    if not req:
        raise HTTPException(status_code=404, detail=f"בקשה {request_id} לא נמצאה")
    return req


@router.get("/customer/{customer_id}", response_model=List[ConcreteRequestResponseDTO])
def get_requests_by_customer(customer_id: int, db: Session = Depends(get_db)):
    """שליפת כל הבקשות של לקוח מסויים"""
    return ConcreteRequestRepository(db).get_by_customer(customer_id)


@router.post("/", response_model=ConcreteRequestResponseDTO, status_code=201)
def create_request(data: ConcreteRequestCreateDTO, db: Session = Depends(get_db)):
    """יצירת בקשת בטון חדשה"""
    return ConcreteRequestRepository(db).create(data)


@router.put("/{request_id}", response_model=ConcreteRequestResponseDTO)
def update_request(
    request_id: int,
    data: ConcreteRequestCreateDTO,
    db: Session = Depends(get_db)
):
    """עדכון בקשת בטון"""
    updated = ConcreteRequestRepository(db).update(request_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"בקשה {request_id} לא נמצאה")
    return updated


@router.delete("/{request_id}", status_code=204)
def delete_request(request_id: int, db: Session = Depends(get_db)):
    """מחיקת בקשה"""
    if not ConcreteRequestRepository(db).delete(request_id):
        raise HTTPException(status_code=404, detail=f"בקשה {request_id} לא נמצאה")
    return None
