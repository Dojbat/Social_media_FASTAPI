from pydantic import BaseModel, ConfigDict

class UserPostIn(BaseModel):
    body: str

class UserPost(UserPostIn):
    model_config = ConfigDict(from_attributes=True)
    id: int

class CommentIn(BaseModel):
    post_id: int
    body: str

class Comment(CommentIn):
    model_config = ConfigDict(from_attributes=True)
    id: int

class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]