from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def return_to_my_view_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='MantisBT']").click()

    def create(self, project):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_to_my_view_page()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//tr[3]/td/a").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.return_to_my_view_page()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        return len(wd.find_elements_by_css_selector("tr.row-1")) + len(wd.find_elements_by_css_selector("tr.row-2"))

    def get_project_list(self):
        wd = self.app.wd
        project_list = []
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        rows = wd.find_elements_by_css_selector(".width100 .row-1") + wd.find_elements_by_css_selector(".width100 .row-2")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            id = None
            name = cells[0].text
            description = cells[4].text
            project_list.append(Project(id=id, name=name, description=description))
        return project_list





