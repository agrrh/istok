from pydantic import BaseModel
from typing import List

from istok.models.item import Item


class BaseItemsList(BaseModel):
    items: List[Item]

    def load_from_dict(items: dict) -> object:
        return BaseItemsList(items=[Item(**i) for i in items.get("items")])

    def to_names_list(self) -> List[str]:
        return [g.name for g in self.items]

    def filter_group(self, group: str) -> object:
        self.items = [i for i in self.items if i.group == group]
        return self
