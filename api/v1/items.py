from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core.database import get_db
from controllers.item_controller import (
    ItemController,
    ItemCreate,
    ItemUpdate,
    ItemResponse
)

router = APIRouter()

@router.get("/items/", response_model=List[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    controller = ItemController(db)
    return controller.get_items(skip=skip, limit=limit)

@router.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    controller = ItemController(db)
    item = controller.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    controller = ItemController(db)
    return controller.create_item(item)

@router.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    controller = ItemController(db)
    updated_item = controller.update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    controller = ItemController(db)
    if not controller.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"status": "success", "message": "Item deleted"} 