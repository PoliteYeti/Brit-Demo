import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from mangum import Mangum

from brit_demo.database import ItemModel, engine, get_db
from brit_demo.schemas import Item, StoredItem, Summary

app = FastAPI(root_path=os.environ.get("ROOT_PATH"))

router = SQLAlchemyCRUDRouter(
    schema=StoredItem,
    create_schema=Item,
    db_model=ItemModel,
    db=get_db,
    prefix="api/items",
)

app.include_router(router)

# Added to enable frontend development from a seperate machine.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/summary", tags=["Summary"], response_model=Summary)
async def get_summary():

    connection = engine.connect()
    # We execute a raw SQL query here as it is much more efficient.
    result = connection.execute("SELECT SUM(price) FROM items")
    totalcost = sum([row[0] for row in result])

    return Summary(totalcost=totalcost)


handler = Mangum(app, lifespan="off")
