from model.project import Project

def test_add_project(app):
    project = Project(name="0name", description="qwerty12")
    #old_projects = app.project.count()
    #old_projects = app.soap.get_list_projects()
    old_projects = app.project.get_project_list()
    app.project.create(project)
    #new_projects = app.project.count()
    #new_projects = app.soap.get_list_projects()
    new_projects = app.project.get_project_list()
    #assert old_projects + 1 == new_projects
    old_projects.append(project)
    assert sorted(old_projects) == sorted(new_projects)