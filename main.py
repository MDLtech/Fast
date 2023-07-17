from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.endpoints import router as api_router
from settings import DATABASE_URL
from tortoise import Tortoise

app = FastAPI()

app.include_router(api_router)

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["db.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.on_event("startup")
async def startup():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["db.models"]}
    )
    await Tortoise.generate_schemas()
