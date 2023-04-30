from fastapi import APIRouter, Depends
from ..database import events_crud as crud
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..database.schemas import EventAllList


router = APIRouter(prefix='/events')


@router.get('', response_model=list[EventAllList])
def fetch_all_events(db: Session = Depends(get_db), type: str = ''):
    return crud.read_all_events(db, type)
