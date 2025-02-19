import os
import re
from templates.main import template as main_template
from templates.index_html import template as html_template
from templates.requirements_txt import template as requirements_template
from templates.docker_file import template as dockerfile_template
from templates.docker_compose import template as docker_compose_template
from templates.gitignore import template as gitignore_template
from templates.readme import template as readme_template
import app.versions as versions


class ProjectBuilder:

    __DOCKER_INPUT_MESSAGE = (
        "Do you want to include Dockerfile and docker-compose.yaml? (y/n) "
    )
    __GITIGNORE_INPUT_MESSAGE = "Do you want to include .gitignore file? (y/n) "
    __project_name: str
    __base_directory: str
    __flask_version: str
    __flask_socketio_version: str
    __is_docker_enabled: bool
    __docker_base_image: str
    __gunicorn_version: str
    __pytest_version: str
    __gevent_version: str
    __is_gitignore_included: str

    def __init__(self, base_directory: str = ""):
        self.__base_directory = base_directory

    def define_project_settings(self):
        self.__project_name = self.__validate_project_name(
            input("Enter the project name: ")
        )
        self.__flask_version = versions.flask
        self.__flask_socketio_version = versions.flask_socketio
        self.__docker_base_image = versions.docker_base_image
        self.__gunicorn_version = versions.gunicorn
        self.__pytest_version = versions.pytest
        self.__gevent_version = versions.gevent
        self.__is_docker_enabled = self.__validate_input(self.__DOCKER_INPUT_MESSAGE)
        self.__is_gitignore_included = self.__validate_input(
            self.__GITIGNORE_INPUT_MESSAGE
        )

    def create_folders_structure(self):
        os.makedirs(f"{self.__base_directory}{self.__project_name}/app")
        with open(
            f"{self.__base_directory}{self.__project_name}/app/__init__.py", "w"
        ) as f:
            f.write("")
        os.makedirs(f"{self.__base_directory}{self.__project_name}/tests")
        with open(
            f"{self.__base_directory}{self.__project_name}/tests/__init__.py", "w"
        ) as f:
            f.write("")
        os.makedirs(f"{self.__base_directory}{self.__project_name}/tests/app")
        with open(
            f"{self.__base_directory}{self.__project_name}/tests/app/__init__.py", "w"
        ) as f:
            f.write("")
        os.makedirs(f"{self.__base_directory}{self.__project_name}/templates")
        os.makedirs(f"{self.__base_directory}{self.__project_name}/static")
        os.makedirs(f"{self.__base_directory}{self.__project_name}/static/js")
        os.makedirs(f"{self.__base_directory}{self.__project_name}/static/img")
        os.makedirs(f"{self.__base_directory}{self.__project_name}/static/css")

    def create_main_py_file(self):
        with open(f"{self.__base_directory}{self.__project_name}/main.py", "w") as f:
            f.write(main_template % self.__project_name)

    def create_index_html_file(self):
        with open(
            f"{self.__base_directory}{self.__project_name}/templates/index.html", "w"
        ) as f:
            f.write(html_template % self.__project_name)

    def create_requirements_txt_file(self):
        with open(
            f"{self.__base_directory}{self.__project_name}/requirements.txt", "w"
        ) as f:
            f.write(
                requirements_template.format(
                    flask_version=self.__flask_version,
                    flask_socketio_version=self.__flask_socketio_version,
                    gunicorn_version=self.__gunicorn_version,
                    pytest_version=self.__pytest_version,
                    gevent_version=self.__gevent_version,
                )
            )

    def create_docker_files(self):
        if self.__is_docker_enabled:
            with open(
                f"{self.__base_directory}{self.__project_name}/Dockerfile", "w"
            ) as f:
                f.write(
                    dockerfile_template.format(
                        docker_base_image=self.__docker_base_image,
                        project_name=self.__project_name,
                    )
                )
            with open(
                f"{self.__base_directory}{self.__project_name}/docker-compose.yaml", "w"
            ) as f:
                f.write(
                    docker_compose_template.format(project_name=self.__project_name)
                )

    def create_gitignore(self):
        if self.__is_gitignore_included:
            with open(
                f"{self.__base_directory}{self.__project_name}/.gitignore", "w"
            ) as f:
                f.write(gitignore_template)

    def create_readme(self):
        with open(f"{self.__base_directory}{self.__project_name}/README.MD", "w") as f:
            f.write(readme_template.format(project_name=self.__project_name))

    def __validate_input(self, input_message: str) -> bool:
        flag = input(input_message)
        while flag not in ["Y", "y", "N", "n"]:
            flag = input(input_message)

        if flag in ["Y", "y"]:
            return True
        return False

    def __validate_project_name(self, project_name: str) -> str:
        reserved_names = {
            "CON",
            "PRN",
            "AUX",
            "NUL",
            "COM1",
            "COM2",
            "COM3",
            "COM4",
            "COM5",
            "COM6",
            "COM7",
            "COM8",
            "COM9",
            "LPT1",
            "LPT2",
            "LPT3",
            "LPT4",
            "LPT5",
            "LPT6",
            "LPT7",
            "LPT8",
            "LPT9",
        }
        folder_name_pattern = r"^[a-zA-Z0-9_\-\. ]+$"

        is_project_name_valid = True

        if not project_name.strip():
            is_project_name_valid = False
        elif project_name.upper() in reserved_names:
            is_project_name_valid = False
        elif not re.match(folder_name_pattern, project_name):
            is_project_name_valid = False

        while not is_project_name_valid:
            project_name = input(
                "Provided project name is incorrect, please, try another one: "
            )

            if not project_name.strip():
                is_project_name_valid = False
            elif project_name.upper() in reserved_names:
                is_project_name_valid = False
            elif not re.match(folder_name_pattern, project_name):
                is_project_name_valid = False
            else:
                is_project_name_valid = True

        return project_name
