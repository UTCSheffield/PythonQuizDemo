from datetime import datetime
from datetime import timezone

from flask import url_for

from PythonQuizDemo import db
from PythonQuizDemo.auth.models import User
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates


def now_utc():
    return datetime.now(timezone.utc)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.ForeignKey(User.id), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=now_utc)
    text = db.Column(db.String(100), nullable=False)
    answer_1 = db.Column(db.String(100), nullable=False)
    answer_2 = db.Column(db.String(100), nullable=False)
    answer_3 = db.Column(db.String(100), nullable=False)
    answer_4 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.Integer(), CheckConstraint("correct_answer>0 and correct_answer<5"), nullable=False)
    author = db.relationship(User, lazy="joined", back_populates="questions")

    @validates("correct_answer")
    def validate_correct_answer(self, key, correct):
        if not (correct>0 and correct<5):
            raise ValueError("Correct Answer must be between 1 & 4")
        return correct
    
    
    @property
    def update_url(self):
        return url_for("quiz.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("quiz.delete", id=self.id)
