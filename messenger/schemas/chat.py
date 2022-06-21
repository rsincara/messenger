from pydantic import BaseModel

from datetime import datetime
from constants.chat import ChatType


class Chat(BaseModel):
    name: str
    type: ChatType


class ChatInDB(Chat):
    id: int
    created_date: datetime

    class Config:
        orm_mode = True


class ChatWithUsers(ChatInDB):
    users: list
