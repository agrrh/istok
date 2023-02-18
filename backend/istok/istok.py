import json
import os
from pathlib import Path
import yaml

from box import Box


class Istok:
    def __init__(self, path: str = "./config.yaml") -> None:
        path = os.environ.get("APP_CONFIG_PATH") or path

        with Path(path).open() as fp:
            self.__data = yaml.load(fp, Loader=yaml.Loader)

    @property
    def _yaml(self) -> str:
        return yaml.dumps(self.__data)

    @property
    def _json(self) -> str:
        return json.dumps(self.__data)

    @property
    def config(self) -> object:
        return Box(self.__data)

    @property
    def groups(self) -> list:
        direct_groups_list = [g.get("name") for g in self.config.groups.get("items")]
        static_groups_list = [i.get("group") for i in self.config.static.get("items")]
        kube_groups_list = []

        return list(set(direct_groups_list + static_groups_list + kube_groups_list))

    def items_by_group(self, group: str) -> list:
        items_static_list = [i for i in self.config.static.get("items") if i.get("group") == group]
        items_kube_list = []

        return list(items_static_list + items_kube_list)
