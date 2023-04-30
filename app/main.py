from fastapi import FastAPI
from .router import events, players

from .database import models
from .database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(events.router)
app.include_router(players.router)

