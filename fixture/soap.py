from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config["web"]["soapUrl"])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_projects(self):
        login = self.app.config["web"]["username"]
        password = self.app.config["web"]["password"]
        client = Client(self.app.config["web"]["soapUrl"])
        project_list = []
        for project in client.service.mc_projects_get_user_accessible(login, password):
            id = project.id
            name = project.name
            description = project.description
            project_list.append(Project(id=id, name=name, description=description))
        return project_list