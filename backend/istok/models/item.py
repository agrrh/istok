from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    group: str
    url: str
    title: Optional[str]
    descr: Optional[str]
    icon: Optional[str] = "mdi:circle-medium"

    def __init__(self, **kwargs) -> None:  # noqa: ANN003
        super().__init__(**kwargs)
        self.title = self.title or self.name.capitalize()
