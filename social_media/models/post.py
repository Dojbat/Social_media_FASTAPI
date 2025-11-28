from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class CommentIn(BaseModel):
    post_id: int
    body: str


class Comment(CommentIn):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]
