from typing import Optional

from app.models.domain.defaultmodel import DefaultModel


class Profile(DefaultModel):
    username: str
    bio: str = ""
    image: Optional[str] = None
    following: bool = False
