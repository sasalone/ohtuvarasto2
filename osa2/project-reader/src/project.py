class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _format_list(self, items):
        if not items:
            return "-"
        return "\n- " + "\n- ".join(items)

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license or '-'}\n\n"
            f"Authors:{self._format_list(self.authors)}\n\n"
            f"Dependencies:{self._format_list(self.dependencies)}\n\n"
            f"Development dependencies:{self._format_list(self.dev_dependencies)}"
        )
