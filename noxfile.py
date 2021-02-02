import nox

# Set the default sessions (really skip the linting)
nox.options.sessions = ["scons"]


@nox.session
def scons(session):
    """Setup and run SCons"""
    session.install("scons", "pikepdf")
    session.run("scons")
    session.run("scons", "-c")


@nox.session
def flake8(session):
    """Run flake8 on the sources"""
    session.install("flake8")
    session.run("flake8", "SConstruct", "noxfile.py")
