from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from .config import settings

engine = create_engine(
    settings.DB_URL,
    future=True,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={"charset": "utf8mb4"},
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)

# ---- Base ----
Base = declarative_base()


# ---- Dependency ----
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()