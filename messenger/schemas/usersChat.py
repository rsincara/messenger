from pydantic import BaseModel


class UsersChat(BaseModel):
    user_id: int
    chat_id: int


class UsersChatInDB(UsersChat):
    id: int

    class Config:
        orm_mode = True
