from model.project import Project

def test_add_project(app):
    login = "administrator"
    password = "root"
    project = Project(name="new3", description="qwerty3")
    #old_projects = app.project.count()
    old_projects = app.soap.get_list_projects(login, password)
    app.project.create(project)
    #new_projects = app.project.count()
    new_projects = app.soap.get_list_projects(login, password)
    #assert old_projects + 1 == new_projects
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
