from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import events, players

from .database import models
from .database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(events.router)
app.include_router(players.router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])
