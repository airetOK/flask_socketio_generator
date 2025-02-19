template = """FROM {docker_base_image}
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /{project_name}
COPY . .
CMD ["gunicorn", "-k", "gevent", "--bind", "0.0.0.0:8000", "main:create_app()"]
EXPOSE 8000"""
