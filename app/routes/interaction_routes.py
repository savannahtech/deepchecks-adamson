import asyncio

from fastapi import APIRouter, Depends, UploadFile, File, BackgroundTasks
from sqlalchemy.orm import Session

from app.controllers.interaction_controller import create_interaction, create_interactions_from_csv
from app.database import SessionLocal
from app.models.interaction import InteractionCreate
from app.routes import SuccessResponse, ErrorResponse

interaction_router = APIRouter()
alert_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def background_create_interaction(input_text: str, output_text: str, db: Session):
    create_interaction(input_text, output_text, db)


async def background_create_interactions_from_csv(csv_data, db: Session):
    create_interactions_from_csv(csv_data.decode('utf-8'), db)


@interaction_router.post("")
async def create_interaction_endpoint(
        background_tasks: BackgroundTasks,
        body: InteractionCreate,
        db: Session = Depends(get_db)
):
    try:
        background_tasks.add_task(background_create_interaction, body.input_text, body.output_text, db)

        return SuccessResponse(data=None, msg="Processing...").to_response()
    except Exception as e:
        return ErrorResponse(error=str(e), status_code=500, msg="Server Error").to_response()


@interaction_router.post("/bulk")
async def create_interactions_from_csv_endpoint(
        background_tasks: BackgroundTasks,
        csv_file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    try:
        csv_data = await csv_file.read()
        background_tasks.add_task(background_create_interactions_from_csv, csv_data, db)

        return SuccessResponse(data=None, msg="Processing...").to_response()
    except Exception as e:
        return ErrorResponse(error=str(e), status_code=500, msg="Server Error").to_response()
