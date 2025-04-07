from fastapi import APIRouter
from api.v1 import items

router = APIRouter()
router.include_router(items.router, tags=["items"]) 