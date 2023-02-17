from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt
from passlib.context import CryptContext
from app import schemas
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"

def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
) -> str:
    expire_obj = datetime.utcnow() + expires_delta
    expire = int(expire_obj.timestamp())
    to_encode = {"exp": expire, "sub": str(subject)}

    return encode_jwt(to_encode)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def encode_jwt(to_encode) -> str:
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    
    
def decode_jwt(token: str) -> dict[str, Any]:
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])


def get_jwt_exp(token: str) -> int:
    payload = decode_jwt(token)
    token_data = schemas.TokenPayload(**payload)
    
    return token_data.exp


def get_jwt_sub(token: str) -> Any:
    payload = decode_jwt(token)
    token_data = schemas.TokenPayload(**payload)
    
    return token_data.sub
