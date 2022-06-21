import schemas.chat as SchemaChat
from sqlalchemy.orm import Session
from core.db.models import Chat
from core.db.models import UsersChat, User


def create_chat(db: Session, chat: SchemaChat.Chat):
    chat_db = Chat(name=chat.name, type=chat.type)
    db.add(chat_db)
    db.commit()

    return chat_db


def get_chat_by_id(db: Session, chat_id: int):
    return db.query(Chat).filter(Chat.id == chat_id).one_or_none()


def update_chat(db: Session, chat_id: int, chat: SchemaChat.Chat):
    chat_db = db.query(Chat).filter(Chat.id == chat_id).one_or_none()
    for param, value in chat.dict().items():
        setattr(chat_db, param, value)
    db.commit()

    return chat_db


def delete_chat(db: Session, chat_id: int):
    db.query(Chat).filter(Chat.id == chat_id).delete()
    db.commit()


def add_user_to_chat(db: Session, user_id: int, chat_id: int):
    user_chat_db = UsersChat(user_id=user_id, chat_id=chat_id)
    db.add(user_chat_db)
    db.commit()

    return get_chat_by_id(db, chat_id=chat_id)


def get_users_by_chat_id(db: Session, chat_id: int):
    return db.query(User.id, User.name, User.login) \
        .join(UsersChat, User.id == UsersChat.user_id) \
        .filter(UsersChat.chat_id == chat_id) \
        .all()


