from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.count()
    app.project.create(Project(name="new1", description="qwerty1"))
    new_projects = app.project.count()
    assert old_projects + 1 == new_projects
