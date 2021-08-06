from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Assessment(Base):
    __tablename__ = "assessment"
    id = Column(Integer, primary_key=True, index=True)
    assessment_version = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email_id = Column(String)
    session_id = Column (String)
    answers = Column(String)
    total_score = Column(Integer)


