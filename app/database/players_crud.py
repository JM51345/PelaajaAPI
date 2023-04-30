from fastapi import HTTPException, status
from .schemas import EventAllList
from sqlalchemy.orm import Session
from . import models


def read_players(db: Session):
    players = db.query(models.Player).all()
    return players


def read_player_by_id(id: int, db: Session):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return player


def read_events_by_id(id: int, db: Session, type: str):
    if type.__eq__(''):
        events = db.query(models.Event).filter(models.Event.player_id == id).all()
    elif type.__eq__('level_started') or type.__eq__('level_solved'):
        events = db.query(models.Event).filter(models.Event.player_id == id).filter(models.Event.type.__eq__(type)).all()
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST) 

    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return events


def save_player(player_in, db: Session):
    player = models.Player(**player_in.dict())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


def save_event(id: int, event_in: EventAllList, db: Session):
    event = models.Event(**event_in.dict(), player_id = id)
    if not db.query(models.Player).filter_by(id=event.player_id).count() > 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    elif not (event.type.__eq__('level_started') or event.type.__eq__('level_solved')):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    db.add(event)
    db.commit()
    db.refresh(event)
    return event