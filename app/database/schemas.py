from pydantic import BaseModel


class EventBase(BaseModel):

    class Config:
        orm_mode = True


class EventAllList(EventBase):
    id: int
    type: str
    detail: str
    timestamp: str
    player_id: int


class PlayersEvents(EventBase):
    id: int
    name: str
    events: list
    

class CreateEvent(EventBase):
    type: str
    detail: str


class PlayerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class PlayerDb(EventBase):
    id: int
    name: str





















