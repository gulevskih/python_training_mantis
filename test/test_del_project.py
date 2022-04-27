from model.project import Project

def test_del_project(app):
    if len(app.soap.get_list_projects()) == 0:
        app.project.create(Project(name="test", description="test"))
    #old_projects = app.project.count()
    old_projects = app.soap.get_list_projects()
    app.project.delete_first_project()
    new_projects = app.soap.get_list_projects()
    #new_projects = app.project.count()
    #assert old_projects - 1 == new_projects
    old_projects[0:1] = []
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)