from fastapi import APIRouter, Depends, HTTPException, status

from deps import get_db
import crud.message as crud

router = APIRouter(prefix="/messages")


@router.post("/send_message")
async def send_message(chat_id: int, user_id: int, text: str, db=Depends(get_db)):
    """Отправить сообщение"""
    result = crud.send_message_in_chat(db=db, chat_id=chat_id, user_id=user_id, text=text)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{message_id}")
async def update_message(message_id: int, text: str, db=Depends(get_db)):
    """Изменить сообщение"""
    result = crud.update_message(db=db, message_id=message_id, text=text)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{message_id}")
async def delete_chat(message_id: int, db=Depends(get_db)):
    """Удалить сообщение"""
    result = crud.delete_message(db=db, message_id=message_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/get_N_last_messages_by_chat_id", response_model=list)
async def get_N_last_messages_in_chat(n: int, chat_id: int, db=Depends(get_db)):
    result = crud.get_N_last_messages_by_chat_id(db=db, n=n, chat_id=chat_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return result


@router.get("/get_N_chats_with_last_activities", response_model=list)
async def get_N_chats_with_last_activities(n: int, db=Depends(get_db)):
    result = crud.get_N_chats_with_last_activities(db=db, n=n)

    return result