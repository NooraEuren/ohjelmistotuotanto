class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors = "\n".join(
            f"- {author['name']}"
            for author in self.authors
        )

        dependencies = "\n".join(
               f"- {dep.split('>=')[0]}"
            for dep in self.dependencies
        )

        dev_dependencies = "\n".join(
             f"- {dep.split('>=')[0]}"
            for dep in self.dev_dependencies
        )

        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license}\n\n"
            f"Authors:\n{authors}\n\n"
                f"Dependencies:\n{dependencies}\n\n"
            f"Development dependencies:\n{dev_dependencies}"
        )
        
