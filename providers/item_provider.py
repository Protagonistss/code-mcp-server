from sqlalchemy.orm import Session
from models.item import Item
from typing import List, Optional

class ItemProvider:
    def __init__(self, db: Session):
        self.db = db

    def get_item(self, item_id: int) -> Optional[Item]:
        return self.db.query(Item).filter(Item.id == item_id).first()

    def get_items(self, skip: int = 0, limit: int = 100) -> List[Item]:
        return self.db.query(Item).offset(skip).limit(limit).all()

    def create_item(self, title: str, description: str) -> Item:
        db_item = Item(title=title, description=description)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update_item(self, item_id: int, title: str = None, description: str = None) -> Optional[Item]:
        db_item = self.get_item(item_id)
        if db_item:
            if title is not None:
                db_item.title = title
            if description is not None:
                db_item.description = description
            self.db.commit()
            self.db.refresh(db_item)
        return db_item

    def delete_item(self, item_id: int) -> bool:
        db_item = self.get_item(item_id)
        if db_item:
            self.db.delete(db_item)
            self.db.commit()
            return True
        return False 