from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.topics.topics import top_topics
from src.forecast.forecast import fake_forecast

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "app": settings.APP_NAME}

@app.get("/topics")
def topics(limit: int = Query(10, ge=1, le=50)):
    return {"items": top_topics(limit=limit)}

@app.get("/forecast")
def forecast(days: int = Query(7, ge=1, le=30)):
    return {"items": fake_forecast(days=days)}
