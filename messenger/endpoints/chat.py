from fastapi import APIRouter, Depends, HTTPException, status

from core.helpers.get_user_or_raise_exception import get_user_or_raise_exception
from deps import get_db, get_current_user
import crud.chat as crud
from schemas.chat import Chat, ChatInDB, ChatWithUsers

router = APIRouter(prefix="/chat")


@router.get("/", response_model=ChatWithUsers)
async def get_chat(chat_id: int, db=Depends(get_db), user_id=Depends(get_current_user)):
    """Получить чат по заданному chat_id"""
    get_user_or_raise_exception(db=db, user_id=user_id)
    chat = crud.get_chat_by_id(db=db, chat_id=chat_id)

    if chat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    users = crud.get_users_by_chat_id(db=db, chat_id=chat_id)
    chat_with_users = ChatWithUsers(id=chat.id, name=chat.name, type=chat.type, users=users,
                                    created_date=chat.created_date)

    return chat_with_users


@router.get("/get_user_chats", response_model=list)
async def get_user_chats(user_id=Depends(get_current_user), db=Depends(get_db)):
    """Получить чаты пользователя"""
    get_user_or_raise_exception(db=db, user_id=user_id)
    chats = crud.get_user_chats(db=db, user_id=user_id)
    return chats


@router.post("/", response_model=ChatInDB)
async def create_chat(chat: Chat, db=Depends(get_db), user_id=Depends(get_current_user)):
    """Создать чат"""
    get_user_or_raise_exception(db=db, user_id=user_id)
    result = crud.create_chat(db=db, chat=chat)
    return result


@router.put("/{chat_id}", response_model=ChatInDB)
async def update_chat(chat: Chat, chat_id: int, db=Depends(get_db), user_id=Depends(get_current_user)):
    """Изменить чат"""
    get_user_or_raise_exception(db=db, user_id=user_id)
    chat_db = crud.update_chat(db=db, chat_id=chat_id, chat=chat)
    return chat_db


@router.delete("/{chat_id}")
async def delete_chat(chat_id: int, db=Depends(get_db)):
    """Удалить чат"""
    crud.delete_chat(db=db, chat_id=chat_id)
