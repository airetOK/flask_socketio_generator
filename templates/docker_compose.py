template = """version: '2.1'
services:
  {project_name}:
    build: .
    image: {project_name}
    container_name: {project_name}
    ports:
      - 5000:8000"""
