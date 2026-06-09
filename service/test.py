"""
בוודאי! הפונקציה שלך עושה את הדברים הבאים בקצרה:
1. מקבלת קבלן (`Contractor`) ורשימת קונים (`Buyer`) יחד עם זמני נסיעה לכל קונה.
2. מסננת את הקונים לפי התאמה: סוג המוצר חייב להיות תואם, כמות הקנייה לא יכולה לעלות על כמות הקבלן, וזמן הנסיעה לא יכול להיות ארוך מדי.
3. מחשבת לכל קונה ציון התאמה (`score`) המבוסס על זמן ההמתנה שלו וזמן הנסיעה.
4. מחזירה רשימה של הקונים המתאימים, ממוינת לפי הציון מהגבוה לנמוך, כך שהקבלן יוכל לבחור את ההתאמה הטובה ביותר.



"""
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List, Dict, Optional

app = FastAPI(title="Buyer Matching API")

# ---------------------------
# מודלים עבור Pydantic
# ---------------------------

class BuyerModel(BaseModel):
    buyer_id: str
    type_: str
    quantity: int
    request_time: datetime
    latitude: float
    longitude: float

class ContractorModel(BaseModel):
    contractor_id: str
    type_: str
    quantity: int
    minutes_left: int
    latitude: float
    longitude: float

class MatchRequest(BaseModel):
    contractor: ContractorModel
    buyers: List[BuyerModel]
    travel_times: Dict[str, int]  # buyer_id -> travel_time_minutes

# ---------------------------
# פונקציות לוגיקה
# ---------------------------

def calculate_match_score(waiting_time_days: float, travel_time_minutes: int, w1: float = 5.0, w2: float = 1.0) -> Optional[float]:
    if travel_time_minutes < 0:
        return None
    score = (w1 * waiting_time_days) - (w2 * travel_time_minutes)
    return score

def filter_and_score_buyers(contractor: ContractorModel, buyers: List[BuyerModel], travel_times: dict) -> List[dict]:
    relevant_buyers = []

    for buyer in buyers:
        if buyer.type_ != contractor.type_:
            continue
        if buyer.quantity > contractor.quantity:
            continue

        travel_time = travel_times.get(buyer.buyer_id, None)
        if travel_time is None or travel_time > contractor.minutes_left:
            continue

        waiting_days = (datetime.now() - buyer.request_time).total_seconds() / (60 * 60 * 24)
        score = calculate_match_score(waiting_days, travel_time)
        if score is not None:
            relevant_buyers.append({
                "buyer_id": buyer.buyer_id,
                "score": score,
                "travel_time_minutes": travel_time,
                "waiting_time_days": waiting_days
            })

    relevant_buyers.sort(key=lambda x: x["score"], reverse=True)
    return relevant_buyers

# ---------------------------
# Endpoint להרצה דרך Postman
# ---------------------------

@app.post("/match")
def match_endpoint(request: MatchRequest):
    return filter_and_score_buyers(request.contractor, request.buyers, request.travel_times)

# ---------------------------
# נתוני דמה לגומא
# ---------------------------

if __name__ == "__main__":
    import uvicorn

    # ניתן להריץ: uvicorn test:app --reload
    print("Running dummy server on http://127.0.0.1:8001")
    uvicorn.run("test:app", host="127.0.0.1", port=8081, reload=True)