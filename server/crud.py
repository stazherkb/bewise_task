from sqlalchemy.orm import Session
import models, schemas


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(q_id=question.q_id, question=question.question,
                                  answer=question.answer, q_date=question.q_date)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_question_by_q_id(db: Session, q_id: int):
    return db.query(models.Question).filter(models.Question.q_id == q_id).first()


def get_all_questions(db: Session):
    return db.query(models.Question).all()


def get_last_question(db: Session):
    return db.query(models.Question).order_by(models.Question.id.desc()).first()