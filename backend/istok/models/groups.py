from pydantic import BaseModel
from typing import List

from istok.models.group import Group
from istok.models.item import Item


class BaseGroupsList(BaseModel):
    items: List[Group]

    def load_from_dict(groups: dict) -> object:
        return BaseGroupsList(items=[Group(**g) for g in groups.get("items")])

    def to_names_list(self) -> List[str]:
        return [g.name for g in self.items]


class DirectGroupsList(BaseGroupsList):
    def load_from_dict(groups: dict) -> object:
        return DirectGroupsList(items=[Group(**g) for g in groups.get("items")])


class StaticGroupsList(BaseGroupsList):
    def load_from_dict(groups: dict) -> object:
        return StaticGroupsList(items=[Group(name=Item(**i).group) for i in groups.get("items")])
