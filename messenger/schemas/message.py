from pydantic import BaseModel

from datetime import datetime
from schemas.user import User
from schemas.chat import Chat


class Message(BaseModel):
    text: str
    isRead: bool
    created_date: datetime
    edited_date: datetime
    user: User
    chat: Chat


class MessageInDB(BaseModel):
    id: int

    class Config:
        orm_mode = True
