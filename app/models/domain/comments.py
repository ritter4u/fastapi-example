from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.defaultmodel import DefaultModel


class Comment(IDModelMixin, DateTimeModelMixin, DefaultModel):
    body: str
    author: Profile
