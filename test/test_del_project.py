from model.project import Project

def test_del_project(app):
    app.session.login("administrator", "root")
    if app.project.count() == 1:
        app.project.create(Project(name="test", description="test"))
    old_projects = app.project.count()
    app.project.delete_first_project()
    new_projects = app.project.count()
    assert old_projects - 1 == new_projects