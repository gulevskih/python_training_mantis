from model.project import Project

def test_add_project(app):
    project = Project(name="new4", description="qwerty4")
    #old_projects = app.project.count()
    old_projects = app.soap.get_list_projects()
    app.project.create(project)
    #new_projects = app.project.count()
    new_projects = app.soap.get_list_projects()
    #assert old_projects + 1 == new_projects
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
