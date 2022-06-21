from fastapi import APIRouter, Depends, HTTPException, status

from core.helpers.get_user_or_raise_exception import get_user_or_raise_exception
from deps import get_db, get_current_user
import crud.message as crud

router = APIRouter(prefix="/messages")


@router.post("/send_message")
async def send_message(chat_id: int, text: str, db=Depends(get_db), user_id=Depends(get_current_user)):
    """Отправить сообщение"""
    user = get_user_or_raise_exception(db=db, user_id=user_id)

    result = crud.send_message_in_chat(db=db, chat_id=chat_id, user_id=user.id, text=text)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{message_id}")
async def update_message(message_id: int, text: str, db=Depends(get_db), user_id=Depends(get_current_user)):
    """Изменить сообщение"""
    user = get_user_or_raise_exception(db=db, user_id=user_id)

    result = crud.update_message(db=db, message_id=message_id, text=text, user_id=user.id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{message_id}")
async def delete_chat(message_id: int, db=Depends(get_db), user_id=Depends(get_current_user)):
    """Удалить сообщение"""
    user = get_user_or_raise_exception(db=db, user_id=user_id)

    result = crud.delete_message(db=db, message_id=message_id, user_id=user.id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/get_N_last_messages_by_chat_id", response_model=list)
async def get_N_last_messages_in_chat(n: int, chat_id: int, db=Depends(get_db), user_id=Depends(get_current_user)):
    user = get_user_or_raise_exception(db=db, user_id=user_id)

    result = crud.get_N_last_messages_by_chat_id(db=db, n=n, chat_id=chat_id, user_id=user.id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return result


@router.get("/get_N_chats_with_last_activities", response_model=list)
async def get_N_chats_with_last_activities(n: int, db=Depends(get_db), user_id=Depends(get_current_user)):
    user = get_user_or_raise_exception(db=db, user_id=user_id)

    result = crud.get_N_chats_with_last_activities(db=db, n=n, user_id=user.id)

    return result