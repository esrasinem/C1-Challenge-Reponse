import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Assessment
from models import Assessment as ModelAssessment
from models import User
from models import User as ModelUser
from schema import Assessment as SchemaAssessment
from schema import User as SchemaUser

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
async def root():
    return {"Message": "Welcome to my response to the C1 Challenge!"}


@app.post("/add-assessment/", response_model=SchemaAssessment)
def add_assessment(assessment: SchemaAssessment):
    db_assessment = ModelAssessment(assessment_version=assessment.assessment_version, user_id=assessment.user_id)
    db.session.add(db_assessment)
    db.session.commit()
    return db_assessment


@app.post("/add-user/", response_model=SchemaUser)
def add_user(user: SchemaUser):
    db_user = ModelUser(
        first_name=user.first_name,
        last_name=user.last_name,
        email_id=user.email_id,
        session_id=user.session_id,
        answers=user.answers,
        total_score=user.total_score,
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user


@app.get("/all-assessments/")
def get_assessments():
    assessments = db.session.query(Assessment).all()

    return assessments


@app.get("/all-users/")
def get_users():
    users = db.session.query(User).all()

    return users


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
