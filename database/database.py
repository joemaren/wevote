
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Date, Integer, String, Column, ForeignKey

Base = declarative_base()

class Poll(Base):
    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    date = Date

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    poll_id = Column(Integer, ForeignKey('poll.id'))

class Response(Base):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    response = Column(String, nullable=False)
