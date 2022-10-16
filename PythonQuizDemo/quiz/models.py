from datetime import datetime
from datetime import timezone

from flask import url_for

from PythonQuizDemo import db
from PythonQuizDemo.auth.models import User


def now_utc():
    return datetime.now(timezone.utc)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.ForeignKey(User.id), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=now_utc)
    text = db.Column(db.String, nullable=False)
    answers = db.relationship("Answer", lazy="joined", back_populates="question")
    author = db.relationship(User, lazy="joined", back_populates="questions")

    @property
    def update_url(self):
        return url_for("quiz.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("quiz.delete", id=self.id)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.ForeignKey(Question.id), nullable=False)
    text = db.Column(db.String, nullable=False)
    correct = db.Column(db.Boolean, nullable=False)
    
    question = db.relationship(Question, lazy="joined", back_populates="answers")
    
    @property
    def update_url(self):
        return url_for("quiz.updatea", id=self.id)

    @property
    def delete_url(self):
        return url_for("quiz.deletea", id=self.id)

