from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl

from app.models.domain.users import User
from app.models.schemas.defaultchema import DefaultSchema


class UserInLogin(DefaultSchema):
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    username: str


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None


class UserWithToken(User):
    token: str


class UserInResponse(DefaultSchema):
    user: UserWithToken
