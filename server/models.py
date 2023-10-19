from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    q_id = Column(Integer, unique=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    q_date = Column(Date, nullable=False)