from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "MCP Server"
    DEBUG: bool = True
    VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api/v1"
    
    # Database settings
    DATABASE_URL: Optional[str] = "sqlite:///./mcp.db"
    
    class Config:
        env_file = ".env"

settings = Settings() 