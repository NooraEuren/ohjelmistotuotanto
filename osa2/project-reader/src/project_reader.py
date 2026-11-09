from urllib import request
from project import Project
import tomllib

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomllib.loads(content)

        project = data["project"]
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            project["name"],
            project["description"],
            project["license"],
            project["authors"],
            project["dependencies"],
            data["dependency-groups"]["dev"]
        )
