from fastapi import FastAPI
from core.config import settings
from api.v1 import router as api_v1_router
from core.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version=settings.VERSION
)

# Include API router
app.include_router(api_v1_router, prefix=settings.API_V1_PREFIX)

@app.get("/")
def read_root():
    return {
        "app_name": settings.APP_NAME,
        "version": settings.VERSION,
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    } 