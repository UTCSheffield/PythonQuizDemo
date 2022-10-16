# PythonQuizDemo

**FIXME** The basic quiz app built in the Flask-SQLAlchemy `tutorial`_, modified into a quiz as proof concept and starting point for student code.

**FIXME** [tutorial](https://flask.palletsprojects.com/tutorial/)

### Aims

To produce a Quiz Web Site using a Python Web Server (Flask), an ORM (SQLAlchemy) and templating (Jinja2) to base student projects on.

## Install

### Install Flask-SQLAlchemy

#### Linux
```bash
python3 -m pip install Flask-SQLAlchemy
```

#### Windows
```dos
py -m pip install -e .
```



### Install PythonQuizDemo:

#### Linux
```bash
python3 -m pip install -e .
```

#### Windows
```dos
py -m pip install -e .
```


## Run

```bash
export FLASK_APP=PythonQuizDemo
export FLASK_DEBUG=true
flask init-db
flask run
```

Or on Windows cmd:

```dos
set FLASK_APP=PythonQuizDemo
set FLASK_DEBUG=true
flask init-db
flask run
```

Or in a restricted windows environment:

```dos
py -m flask --app=PythonQuizDemo init-db
py -m flask --app=PythonQuizDemo --debug run
```

Open http://127.0.0.1:5000 in a browser.

<!--
## Test **FIXME**


.. code-block:: text

    $ pip install -e '.[test]'
    $ pytest

Run with coverage report:

.. code-block:: text

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser

-->