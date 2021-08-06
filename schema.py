from pydantic import BaseModel


class Assessment(BaseModel):
    assessment_version: str
    user_id: int

    class Config:
        orm_mode = True




class User(BaseModel):
    first_name: str
    last_name: str
    email_id: str
    session_id: str
    answers: str
    total_score: int

    class Config:
        orm_mode = True
