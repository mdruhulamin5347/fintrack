from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from functools import lru_cache

class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )
    
    APP_NAME: str = "FinTrack"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    ENVIROMENT: str = "development"
    
    HOST: str = "0.0.0.0"
    PORT: str = "8000"
    WORKERS: int = 1
    
    SECRET_KEY: str = Field(..., min_length=32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()