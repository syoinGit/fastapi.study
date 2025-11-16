from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .core.db import Base, engine

from .schemas import user
from .api.v1.users import users

app = FastAPI()

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