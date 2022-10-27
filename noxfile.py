import nox


nox.options.reuse_existing_virtualenvs = True

@nox.session
def init(session):
    session.install("-r", "venv-config/requirements.txt")
    session.run("python", "-m", "ipykernel", "install", "--user", "--name=iris", "--display-name", "Python 3.9 (iris)")


@nox.session
def lint(session):
    session.install("-r", "venv-config/requirements.txt")
    session.install("flake8")
    session.run("flake8", "noxfile.py")
