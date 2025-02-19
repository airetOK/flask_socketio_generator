from flask_socket_generator_app.project_builder import ProjectBuilder


class ProjectManager:

    __builder: ProjectBuilder

    def __init__(self, builder: ProjectBuilder):
        self.__builder = builder

    def create_project(self):
        self.__builder.define_project_settings()
        self.__builder.create_folders_structure()
        self.__builder.create_main_py_file()
        self.__builder.create_index_html_file()
        self.__builder.create_requirements_txt_file()
        self.__builder.create_docker_files()
        self.__builder.create_gitignore()
        self.__builder.create_readme()
