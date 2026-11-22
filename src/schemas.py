from pydantic import BaseModel, ConfigDict, Field


class PlayerCreate(BaseModel):
    name: str = Field(min_length=1, max_length=20)


class Player(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    best_score: int | None
