import nox

@nox.session
def scons(session):
    """Setup and run SCons"""
    session.install("scons", "pikepdf")
    session.run("scons")
    session.run("scons", "-c")
