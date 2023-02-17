from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int
    exp: int


class TokenCreate(BaseModel):
    access_token: str
    expires_in: int