from app.project_manager import ProjectManager
from app.project_builder import ProjectBuilder

builder = ProjectBuilder()
project_manager = ProjectManager(builder)


def main():
    project_manager.create_project()  # Call the function inside `main()`


if __name__ == "__main__":
    main()
