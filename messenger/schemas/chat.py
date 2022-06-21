from pydantic import BaseModel

from datetime import datetime
from constants.chat import ChatType
from schemas.user import UserInDB


class Chat(BaseModel):
    name: str
    type: ChatType


class ChatCreate(Chat):
    created_date: datetime


class ChatInDB(Chat):
    id: int

    class Config:
        orm_mode = True


class ChatWithUsers(ChatInDB):
    users: list
