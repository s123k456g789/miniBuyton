from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Optional

app = FastAPI(title="Concrete Matching - Rudy")

# ---------------------------
# מודלים לפי הטבלאות שלך
# ---------------------------

class ContractorModel(BaseModel):
    contractor_id: int
    first_name: str
    last_name: str
    user_name: str
    password: str
    phone: str

class ConcreteRequestModel(BaseModel):
    request_id: int
    customer_id: int
    purpose_id: int
    quantity: float
    address: str
    lat: float
    lng: float
    date: datetime
    region: str

class RudyRequest(BaseModel):
    contractor: ContractorModel
    requests: List[ConcreteRequestModel]
    travel_times: Dict[int, int]  # request_id -> minutes


# ---------------------------
# לוגיקה
# ---------------------------

def calculate_score(waiting_days: float, travel_minutes: int):
    return (5 * waiting_days) - (1 * travel_minutes)


def filter_requests(contractor: ContractorModel,
                    requests: List[ConcreteRequestModel],
                    travel_times: dict):

    results = []

    for r in requests:

        travel = travel_times.get(r.request_id)

        if travel is None:
            continue

        # תנאי זמן נסיעה (דמוי "בטון מתקשה")
        if travel > 60:
            continue

        waiting_days = (datetime.now() - r.date).total_seconds() / 86400

        score = calculate_score(waiting_days, travel)

        results.append({
            "request_id": r.request_id,
            "customer_id": r.customer_id,
            "contractor_id": contractor.contractor_id,
            "score": score,
            "travel_minutes": travel,
            "waiting_days": waiting_days
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)


# ---------------------------
# endpoint RUDY
# ---------------------------

@app.post("/rudy")
def rudy(data: RudyRequest):
    return filter_requests(data.contractor, data.requests, data.travel_times)


# ---------------------------
# הרצה
# ---------------------------

if __name__ == "__main__":
    import uvicorn
    print("Server running: http://127.0.0.1:8081")
    uvicorn.run("test2:app", host="127.0.0.1", port=8081, reload=True)