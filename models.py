from pydantic import BaseModel, Field

class PetPost(BaseModel):
    body = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }


class Tag(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    category: Category
    name: str = Field(alias="SuperDog")
    photoUrls: str
    tags: Tag
    status: str = Field(alias="available")
