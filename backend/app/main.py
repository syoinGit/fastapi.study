from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .core.db import Base, engine
from .api.v1 import users

class UTF8JSONResponse(JSONResponse):
    media_type = "application/json; charset=utf-8"

app = FastAPI(default_response_class=UTF8JSONResponse)
app.add_middleware(
CORSMiddleware,
allow_origins=settings.CORS_ORIGINS,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# 学習・開発中のみ（本番は Alembic）
Base.metadata.create_all(bind=engine)

API_PREFIX = "/api/v1"
app.include_router(users.router,  prefix=API_PREFIX)