import datetime
from sqlalchemy.orm import Session
from core.db.models import Chat
from core.db.models import Message
from core.db.models import User
from crud.chat import get_users_by_chat_id, get_chat_by_id

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


def get_N_last_messages_by_chat_id(db: Session, n: int, chat_id: int):
    chat = get_chat_by_id(db=db, chat_id=chat_id)

    if chat is None:
        return False

    return db.query(Message).filter(Message.chat_id == chat_id).order_by(Message.created_date.desc()).limit(n).all()

def get_N_chats_with_last_activities(db: Session, n: int):
    query_text = f"select * from (select chat_id, max(edited_date) as last_activity_date from messages group by chat_id) as foo order by last_activity_date desc limit {n}"
    result = db.execute(query_text).all()

    return result
