from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from PythonQuizDemo import db
from PythonQuizDemo.auth.views import login_required
from PythonQuizDemo.quiz.models import Question, Answer

bp = Blueprint("quiz", __name__)


@bp.route("/")
def index():
    """Show all the questions, most recent first."""
    select = db.select(Question).order_by(Question.created.desc())
    questions = db.session.execute(select).scalars().unique()
    return render_template("quiz/index.html", questions=questions)


def get_question(id, check_author=True):
    """Get a question and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of question to get
    :param check_author: require the current user to be the author
    :return: the question with author information
    :raise 404: if a question with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    question = db.get_or_404(Question, id, description=f"Question id {id} doesn't exist.")

    if check_author and question.author != g.user:
        abort(403)

    return question


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new question for the current user."""
    if request.method == "POST":
        text = request.form["text"]
        #body = request.form["body"]
        error = None

        if not text:
            error = "Question Text is required."

        if error is not None:
            flash(error)
        else:
            db.session.add(Question(text=text, author=g.user))
            db.session.commit()
            return redirect(url_for("quiz.index"))

    return render_template("quiz/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a question if the current user is the author."""
    question = get_question(id)

    if request.method == "POST":
        text = request.form["text"]
        print("request.form", request.form)
        new_answers = request.form["answers"]
        
        
        error = None

        if not text:
            error = "Question Text is required."

        if error is not None:
            flash(error)
        else:
            question.text = text
            #question.body = body
            db.session.commit()
            return redirect(url_for("quiz.index"))

    return render_template("quiz/update.html", question=question)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a question.

    Ensures that the question exists and that the logged in user is the
    author of the question.
    """
    question = get_question(id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for("quiz.index"))
