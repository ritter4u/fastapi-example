from typing import List, Optional

from pydantic import BaseModel, Field

from app.models.domain.articles import Article
from app.models.schemas.defaultchema import DefaultSchema

DEFAULT_ARTICLES_LIMIT = 20
DEFAULT_ARTICLES_OFFSET = 0


class ArticleForResponse(DefaultSchema, Article):
    tags: List[str] = Field(..., alias="tagList")


class ArticleInResponse(DefaultSchema):
    article: ArticleForResponse


class ArticleInCreate(DefaultSchema):
    title: str
    description: str
    body: str
    tags: List[str] = Field([], alias="tagList")


class ArticleInUpdate(DefaultSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    body: Optional[str] = None


class ListOfArticlesInResponse(DefaultSchema):
    articles: List[ArticleForResponse]
    articles_count: int


class ArticlesFilters(BaseModel):
    tag: Optional[str] = None
    author: Optional[str] = None
    favorited: Optional[str] = None
    limit: int = Field(DEFAULT_ARTICLES_LIMIT, ge=1)
    offset: int = Field(DEFAULT_ARTICLES_OFFSET, ge=0)
