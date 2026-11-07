from urllib import request
import toml
import re
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        
        project_data = parsed_toml.get("project", {})
        
        name = project_data.get("name", "Nimi puuttuu")
        description = project_data.get("description", "Kuvaus puuttuu")
        license = project_data.get("license", "-")
        
        # Tekijöiden nimet
        authors_data = project_data.get("authors", [])
        authors = [author.get("name") for author in authors_data if "name" in author]
        
        # Haetaan riippuvuudet ja siivotaan versiointimerkit
        raw_deps = project_data.get("dependencies", [])
        dependencies = [re.split(r'[>=<~]', dep)[0].strip() for dep in raw_deps]
        
        dependency_groups = parsed_toml.get("dependency-groups", {})
        raw_dev_deps = dependency_groups.get("dev", [])
        dev_dependencies = [re.split(r'[>=<~]', dep)[0].strip() for dep in raw_dev_deps]

        # Palautetaan olio
        return Project(name, description, license, authors, dependencies, dev_dependencies)
