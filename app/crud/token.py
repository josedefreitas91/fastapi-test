from typing import Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models import Token
from app.schemas import TokenCreate


class CRUDToken(CRUDBase[Token, TokenCreate, TokenCreate]):
    def get(self, db: Session, *, token: str) -> Optional[Token]:
        return db.query(Token).filter(Token.access_token == token).first()


    def create(self, db: Session, *, data: TokenCreate) -> Token:
        new_token = Token(access_token=data.access_token, expires_in=data.expires_in) # type: ignore
        db.add(new_token)
        db.commit()
        db.refresh(new_token)
        return new_token


    def remove(self, db: Session, *, token: str) -> Optional[Token]:
        obj = db.query(Token).get(token)
        db.delete(obj)
        db.commit()
        return obj


    # def update(
    #     self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    # ) -> User:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     if update_data["password"]:
    #         hashed_password = get_password_hash(update_data["password"])
    #         del update_data["password"]
    #         update_data["hashed_password"] = hashed_password
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)


token = CRUDToken(Token)
