import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from istok.istok import Istok

app = FastAPI()

# FIXME: Dev mode only!
origins = [
    "http://127.0.0.1:5000",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
