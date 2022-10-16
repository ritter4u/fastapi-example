from typing import List

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.defaultmodel import DefaultModel


class Article(IDModelMixin, DateTimeModelMixin, DefaultModel):
    slug: str
    title: str
    description: str
    body: str
    tags: List[str]
    author: Profile
    favorited: bool
    favorites_count: int
