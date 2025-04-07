from typing import List, Optional
from providers.item_provider import ItemProvider
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ItemResponse(ItemBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ItemController:
    def __init__(self, db: Session):
        self.provider = ItemProvider(db)

    def get_item(self, item_id: int) -> Optional[ItemResponse]:
        item = self.provider.get_item(item_id)
        return ItemResponse.model_validate(item) if item else None

    def get_items(self, skip: int = 0, limit: int = 100) -> List[ItemResponse]:
        items = self.provider.get_items(skip, limit)
        return [ItemResponse.model_validate(item) for item in items]

    def create_item(self, item: ItemCreate) -> ItemResponse:
        db_item = self.provider.create_item(title=item.title, description=item.description)
        return ItemResponse.model_validate(db_item)

    def update_item(self, item_id: int, item: ItemUpdate) -> Optional[ItemResponse]:
        db_item = self.provider.update_item(
            item_id,
            title=item.title,
            description=item.description
        )
        return ItemResponse.model_validate(db_item) if db_item else None

    def delete_item(self, item_id: int) -> bool:
        return self.provider.delete_item(item_id) 