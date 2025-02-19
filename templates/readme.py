template = """# {project_name}
## Usage
- Run from Docker
  - Execute **docker-compose up** from the project's root. The app lives on *localhost:5000*.
- Run locally
  - create virtual environment **python -m venv venv**
  - activate venv **cd venv/Scripts**, from Scripts folder execute **activate**
  - from the project's root execute **pip install -r requirements.txt**
  - from the project's root execute **flask --app main run**. The app lives on *localhost:5000*.
## Notes
Add your own modules to the /app folder.
Feel free to modify the dependencies versions in requirements.txt or the base image in Dockerfile, but on your own reponsibility.
"""
