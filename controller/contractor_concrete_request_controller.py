"""
Controller להצעות של קבלנים (ContractorConcreteRequest)
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from dto.contractor_concrete_request_dto import (
    ContractorConcreteRequestCreateDTO,
    ContractorConcreteRequestResponseDTO,
)
from repository.contractor_concrete_request_repository import ContractorConcreteRequestRepository


router = APIRouter(
    prefix="/contractor-offers",
    tags=["Contractor Offers"]
)


@router.get("/", response_model=List[ContractorConcreteRequestResponseDTO])
def get_all_offers(
    region: str = Query(None, description="סינון לפי אזור"),
    db: Session = Depends(get_db)
):
    """שליפת כל ההצעות של קבלנים"""
    repo = ContractorConcreteRequestRepository(db)
    if region:
        return repo.get_by_region(region)
    return repo.get_all()


@router.get("/{request_id}", response_model=ContractorConcreteRequestResponseDTO)
def get_offer(request_id: int, db: Session = Depends(get_db)):
    """שליפת הצעה לפי מזהה"""
    offer = ContractorConcreteRequestRepository(db).get_by_id(request_id)
    if not offer:
        raise HTTPException(status_code=404, detail=f"הצעה {request_id} לא נמצאה")
    return offer


@router.get("/contractor/{contractor_id}", response_model=List[ContractorConcreteRequestResponseDTO])
def get_offers_by_contractor(contractor_id: int, db: Session = Depends(get_db)):
    """שליפת כל ההצעות של קבלן מסויים"""
    return ContractorConcreteRequestRepository(db).get_by_contractor(contractor_id)


@router.post("/", response_model=ContractorConcreteRequestResponseDTO, status_code=201)
def create_offer(data: ContractorConcreteRequestCreateDTO, db: Session = Depends(get_db)):
    """יצירת הצעת קבלן חדשה"""
    return ContractorConcreteRequestRepository(db).create(data)


@router.put("/{request_id}", response_model=ContractorConcreteRequestResponseDTO)
def update_offer(
    request_id: int,
    data: ContractorConcreteRequestCreateDTO,
    db: Session = Depends(get_db)
):
    """עדכון הצעת קבלן"""
    updated = ContractorConcreteRequestRepository(db).update(request_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"הצעה {request_id} לא נמצאה")
    return updated


@router.delete("/{request_id}", status_code=204)
def delete_offer(request_id: int, db: Session = Depends(get_db)):
    """מחיקת הצעת קבלן"""
    if not ContractorConcreteRequestRepository(db).delete(request_id):
        raise HTTPException(status_code=404, detail=f"הצעה {request_id} לא נמצאה")
    return None
