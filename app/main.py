from fastapi import FastAPI
from app.database import init_db
from app.routes.alert_routes import alert_router
from app.routes.interaction_routes import interaction_router


app = FastAPI()


@app.on_event("startup")
async def startup():
    await init_db()


app.include_router(interaction_router, prefix="/api/interactions", tags=["interactions"])
app.include_router(alert_router, prefix="/api/alerts", tags=["alerts"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
