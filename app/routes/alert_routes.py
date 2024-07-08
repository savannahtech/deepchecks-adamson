from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.controllers.alert_controller import get_alerts
from app.database import SessionLocal
from app.routes import SuccessResponse, ErrorResponse

alert_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@alert_router.get("")
async def get_alerts_endpoint(interaction_id: int = Query(None), db: Session = Depends(get_db)):
    try:
        alerts = get_alerts(db, interaction_id)

        # data = []
        # for alert in alerts:
        #     data.append(alert.as_dict())

        return SuccessResponse(data=alerts).to_response()
    except Exception as e:
        return ErrorResponse(error=str(e), status_code=500, msg="Server Error").to_response()
