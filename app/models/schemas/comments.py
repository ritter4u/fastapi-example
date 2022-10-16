from typing import List

from app.models.domain.comments import Comment
from app.models.schemas.defaultchema import DefaultSchema


class ListOfCommentsInResponse(DefaultSchema):
    comments: List[Comment]


class CommentInResponse(DefaultSchema):
    comment: Comment


class CommentInCreate(DefaultSchema):
    body: str
