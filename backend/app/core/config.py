from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    DB_URL: str
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    model_config = {"env_file": ".env", "extra": "ignore"}

settings = Settings()