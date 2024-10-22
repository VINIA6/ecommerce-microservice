from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: Optional[str] = None  # Corrigido para usar Optional
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
