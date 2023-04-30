from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'))
    timestamp = Column(String, default=func.now())

    player = relationship('Player', back_populates='events')


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    events = relationship('Event', back_populates='player')
