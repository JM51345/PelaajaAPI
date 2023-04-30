from fastapi import APIRouter, Depends, status
from ..database import players_crud as crud
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..database.schemas import CreateEvent, EventAllList, PlayerBase, PlayerDb, PlayersEvents


router = APIRouter(prefix='/players')


@router.get('', response_model=list[PlayerDb])
def fetch_players(db: Session = Depends(get_db)):
    players = crud.read_players(db)
    return players


@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase, db: Session = Depends(get_db)):
    return crud.save_player(player_in, db)


@router.get('/{id}', response_model=PlayersEvents)
def fetch_player_info(id: int, db: Session = Depends(get_db)):
    return crud.read_player_by_id(id, db)


@router.get('/{id}/events', response_model=list[EventAllList])
def fetch_player_events(id: int, db: Session = Depends(get_db), type: str = ''):
    return crud.read_events_by_id(id, db, type)


@router.post('/{id}/events', response_model=EventAllList, status_code=status.HTTP_201_CREATED)
def create_new_event(id: int, event_in: CreateEvent, db: Session = Depends(get_db)):
    return crud.save_event(id, event_in, db)
