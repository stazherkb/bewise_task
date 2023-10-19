from pydantic import BaseModel


class QuestionBase(BaseModel):
    q_id: int
    question: str
    answer: str
    q_date: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True
