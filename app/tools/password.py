from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError
from app.core.config import settings
from app.core import security

def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = security.encode_jwt({"exp": exp, "nbf": now, "sub": email})
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = security.decode_jwt(token)
        return decoded_token["email"]
    except JWTError:
        return None