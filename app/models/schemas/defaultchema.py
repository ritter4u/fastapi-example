from app.models.domain.defaultmodel import DefaultModel


class DefaultSchema(DefaultModel):
    class Config(DefaultModel.Config):
        orm_mode = True
