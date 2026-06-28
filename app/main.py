from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.Person import router as PersonRouter

app = FastAPI(title="Backend template with alembic")

app.include_router(PersonRouter)

