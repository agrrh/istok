from pydantic import BaseModel
from typing import Optional, List

from istok.models.item import Item


class Group(BaseModel):
    name: str
    title: Optional[str]
    items: Optional[List[Item]]

    def __init__(self, **kwargs) -> None:  # noqa: ANN003
        super().__init__(**kwargs)
        self.title = self.title or self.name.capitalize()
