import json
import os
from pathlib import Path
import yaml

from box import Box

from istok.models.groups import BaseGroupsList, DirectGroupsList, StaticGroupsList
from istok.models.items import BaseItemsList


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
        direct_groups_list = DirectGroupsList.load_from_dict(self.config.groups)
        static_groups_list = StaticGroupsList.load_from_dict(self.config.static)
        kube_groups = {"items": []}
        kube_groups_list = BaseGroupsList.load_from_dict(kube_groups)

        result_list = []

        result_list += direct_groups_list.to_names_list()
        result_list += set(static_groups_list.to_names_list()).difference(result_list)
        result_list += set(kube_groups_list.to_names_list()).difference(result_list)

        return result_list

    def items_by_group(self, group: str) -> list:
        items_static_list = BaseItemsList.load_from_dict(self.config.static)

        items_kube_list = []

        return list(items_static_list.filter_group(group).items + items_kube_list)
