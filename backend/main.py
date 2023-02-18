import uvicorn
from fastapi import FastAPI

from istok.istok import Istok

app = FastAPI()

i = Istok()


@app.get("/")
def read_root() -> None:
    repo_base_url = "https://github.com/agrrh/istok"
    return {
        "github": f"{repo_base_url}",
        "docs": f"{repo_base_url}/blob/master/README.md",
        "config": f"{repo_base_url}/blob/master/backend/config.example.yaml",
    }


@app.get("/config/")
def read_config() -> None:
    return i.config


@app.get("/groups/")
def read_groups() -> None:
    return i.groups


@app.get("/items/{group}/")
def read_items(group: str) -> None:
    return i.items_by_group(group)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=True)
