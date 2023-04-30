from fastapi import HTTPException, status
#from .schemas import EventBase, EventDb
from sqlalchemy.orm import Session
from . import models


def read_all_events(db: Session, type: str):
    if type.__eq__('level_started') or type.__eq__('level_solved'):
        events = db.query(models.Event).filter(models.Event.type == type).all()
    elif type.__eq__(''):
        events = db.query(models.Event).all()
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return events