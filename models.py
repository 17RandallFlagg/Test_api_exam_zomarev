from pydantic import BaseModel, ConfigDict
from typing import Optional
import enum_statuses


class Tag(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    category: Optional[Category] = None
    name: Optional[str] = None
    photoUrls: Optional[list[str]] = None
    tags: Optional[list[Tag]] = None
    status: enum_statuses.EnumStatuses
