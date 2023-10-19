from datetime import datetime
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database, models, schemas, crud
from typing import List, Union
from pydantic import BaseModel
from pydantic import Field
import requests

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Bewise.ai",
    description="Bewise test app",
    version="0.0.1",
    docs_url="/docs"
)

@app.get("/questions/{questions_num}")
def get_questions(questions_num: int, db: Session = Depends(database.get_db)):
    alls = crud.get_all_questions(db)
    last_question: Union[models.Question, None] = crud.get_last_question(db)
    # first check if none
    if last_question:
        # MAke q_date readable
        last_question.q_date = last_question.q_date.strftime("%Y-%m-%d")
        last_question_JSON = last_question.__dict__.copy()
        last_question_JSON.pop('_sa_instance_state')
        print(f'Last question is: {last_question.question}')
        print(f'Last question is: {last_question_JSON}')
    # print(f'All questions are: {alls}')
    # print(f'alls[0]: {alls[0].answer}')
    # print('type(alls): ', type(alls))


@app.post("/questions/{questions_num}")
def get_questions(questions_num: int, db: Session = Depends(database.get_db)):
    # Return last question from db, or None if none exists
    print(f'Last question is: {crud.get_last_question(db)}')
    # print all questions
    # print(f'All questions are: {crud.get_all_questions(db)}')
    print(crud.get_all_questions(db))

    last_question: Union[models.Question, None] = crud.get_last_question(db)

    for _ in range(questions_num):
        while True:
            response = requests.get(
                f"https://jservice.io/api/random?count=1"
                )
            jres = response.json()
            question = models.Question(
                q_id=jres[0]["id"],
                question=jres[0]["question"],
                answer=jres[0]["answer"],
                # q_date=jres[0]["created_at"] # datetime.datetime.strptime(jres[0]["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
                q_date=datetime.strptime(jres[0]["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
            )

            # Check if the question already exists in the database
            db_question = crud.get_question_by_q_id(db, jres[0]["id"])

            if db_question is None:
                # If the question does not exist, create it
                crud.create_question(db, question)
                break

    return last_question
