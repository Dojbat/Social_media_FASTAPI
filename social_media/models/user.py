from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    email: str


# easier to return user without password
class UserIn(User):
    password: str
