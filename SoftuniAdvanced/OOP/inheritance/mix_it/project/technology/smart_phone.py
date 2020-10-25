from project.technology.laptop import Laptop


class SmartPhone(Laptop):

    def install_apps(self, app, app_memory):
        return self.install_software(app, app_memory)
