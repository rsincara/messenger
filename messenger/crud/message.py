import datetime
from sqlalchemy.orm import Session
from core.db.models import Chat
from core.db.models import Message
from core.db.models import UsersChat, User
from crud.chat import get_users_by_chat_id


def send_message_in_chat(db: Session, user_id: int, chat_id: int, text: str):
    user = db.query(User).filter(User.id == user_id).one_or_none()
    chat = db.query(Chat).filter(Chat.id == chat_id).one_or_none()

    is_user_in_chat = False
    if user is None:
        return False

    if chat is None:
        return False
    else:
        chat_users = get_users_by_chat_id(db=db, chat_id=chat.id)
        for chat_user in chat_users:
            chat_user_id = chat_user[0]
            if chat_user_id == user_id:
                is_user_in_chat = True
                break

    if not is_user_in_chat:
        return False

    message_db = Message(user_id=user_id, chat_id=chat_id, text=text)
    db.add(message_db)
    db.commit()

    return True


def update_message(db: Session, message_id: int, text: str):
    message_db = db.query(Message).filter(Message.id == message_id).one_or_none()
    if message_db is None:
        return False

    setattr(message_db, 'text', text)
    setattr(message_db, 'edited_date', datetime.datetime.now())
    db.commit()

    return True


def delete_message(db: Session, message_id: int):
    query = db.query(Message).filter(Message.id == message_id)
    message_db = query.one_or_none()

    if message_db is None:
        return False

    query.delete()
    db.commit()

    return True