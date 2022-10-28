import nox
import sys
import pkg_resources
import pprint


nox.options.reuse_existing_virtualenvs = True

@nox.session
def init(session):
    session.install("-r", "venv-config/requirements.txt")
    print(sys.path)
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
       for i in installed_packages])
    pprint.pprint(installed_packages_list)

    #session.run("python", "-m", "ipykernel", "install", "--user", "--name=iris", "--display-name", "Python 3.9 (iris)")


@nox.session
def lint(session):
    session.install('--quiet', "-r", "venv-config/requirements.txt")
    session.install("flake8")
    session.run("flake8", "noxfile.py")


@nox.session
def lint_notebooks(session):
    # flakehell requieres toml
    # session.install('flake8', 'flakehell')
    # session.run(
    #        'flakehell',
    #        'lint',
    #        './notebooks/')
    session.install('--quiet', "-r", "venv-config/requirements.txt")
    session.install('nblint')

    import os
    for root, dirs, files in os.walk('./notebooks/'):
        if 'output' not in root:
            for name in files:
                if name.endswith('.ipynb'):
                    if 'checkpoint' not in name:
                        filename = os.path.join(root, name)
                        session.run(
                                'nblint',
                                '--linter',
                                'pyflakes',
                                filename)
    # TODO ignore magic
