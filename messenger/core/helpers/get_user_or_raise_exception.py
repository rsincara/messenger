import crud.user as user_crud
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_user_or_raise_exception(db: Session, user_id: int):
    user = user_crud.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user
