import os
import shutil
import pytest
from app.project_manager import ProjectManager
from app.project_builder import ProjectBuilder


__BASE_DIRECTORY = "tests/"
__PROJECT_NAME = "test_project"


@pytest.fixture()
def project_manager():
    return ProjectManager(ProjectBuilder(base_directory=__BASE_DIRECTORY))


@pytest.fixture()
def clean_up():
    yield
    shutil.rmtree(f"{__BASE_DIRECTORY}{__PROJECT_NAME}")


def test_project_creation_with_docker_files_and_gitignore(
    project_manager, monkeypatch, clean_up
):
    responses = {
        "Enter the project name: ": __PROJECT_NAME,
        "Do you want to include Dockerfile and docker-compose.yaml? (y/n) ": "y",
        "Do you want to include .gitignore file? (y/n) ": "y",
    }

    monkeypatch.setattr("builtins.input", lambda prompt: responses.get(prompt, ""))
    project_manager.create_project()

    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/app")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static/js")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static/img")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static/css")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/templates")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests/app")

    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/app/__init__.py")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/templates/index.html")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests/__init__.py")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests/app/__init__.py")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/main.py")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/docker-compose.yaml")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/Dockerfile")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/README.MD")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/.gitignore")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/requirements.txt")


def test_project_creation_with_docker_files_and_gitignore(
    project_manager, monkeypatch, clean_up
):
    responses = {
        "Enter the project name: ": __PROJECT_NAME,
        "Do you want to include Dockerfile and docker-compose.yaml? (y/n) ": "n",
        "Do you want to include .gitignore file? (y/n) ": "n",
    }

    monkeypatch.setattr("builtins.input", lambda prompt: responses.get(prompt, ""))
    project_manager.create_project()

    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/app")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static/js")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static/img")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/static/css")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/templates")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests")
    assert os.path.isdir(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests/app")

    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/app/__init__.py")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/templates/index.html")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests/__init__.py")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/tests/app/__init__.py")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/main.py")
    assert not os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/docker-compose.yaml")
    assert not os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/Dockerfile")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/README.MD")
    assert not os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/.gitignore")
    assert os.path.isfile(f"{__BASE_DIRECTORY}{__PROJECT_NAME}/requirements.txt")
