from fastapi.params import Depends
from starlette.middleware.sessions import Session

from controller.concrete_type_controller import router
from database import get_db
from dto import testDto
from repository import ContractorConcreteRequestRepository


@router.post("/find-candidates")
def find_candidates(
    request: testDto,
    db: Session = Depends(get_db())
):
    repo = ContractorConcreteRequestRepository(db)

    return repo.get_candidate_requests(
        lat=request.lat,
        lng=request.lng,
        concrete_id=request.concrete_id,
        required_quantity=request.quantity,
        radius_meters=10000
    )