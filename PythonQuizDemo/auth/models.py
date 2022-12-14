from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from PythonQuizDemo import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    
    # posts = db.relationship("Post", back_populates="author")
    questions = db.relationship("Question", back_populates="author")
    
    def __repr__(self) -> str:
        return self.username

    def set_password(self, value):
        """Store the password as a hash for security."""
        self.password_hash = generate_password_hash(value)

    # allow password = "..." to set a password
    password = property(fset=set_password)

    def check_password(self, value):
        return check_password_hash(self.password_hash, value)
