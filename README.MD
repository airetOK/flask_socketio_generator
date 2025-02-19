# Flask-SocketIO-Generator
Flask-SocketIO-Generator is a tool for generating a template project structure for a Flask application with Socket.IO integration. The tool automatically sets up an initial folder structure, includes the necessary Docker files, a .gitignore, and a Socket.IO client in the HTML files.

With Flask-SocketIO-Generator, you can quickly bootstrap a Flask application with real-time capabilities, reducing the manual setup time and getting you started faster.

## Features
- Generates a basic Flask app template with Socket.IO configuration.
- Automatically creates the folder structure for your Flask project.
- Includes Docker configuration files for easy containerization.
- Sets up a .gitignore for ignoring common unnecessary files.
- Adds a Socket.IO client to the HTML for seamless communication with the server.

## HOT TO INSTALL AND RUN
**pip install flask_socketio_generator**  
Run command **flask_socketio_generate**

## HOW TO RUN LOCALLY:
- **git clone https://github.com/airetOK/flask_socketio_generator.git**
- create virtual environment **python -m venv venv**
- activate venv **cd venv/Scripts**, from Scripts folder execute **activate**
- from the project's root execute **pip install -r requirements.txt**
- from the project's root execute **python -m app.main**

## USAGE
The command **python -m api.main** will ask you to enter project name, include docker support and add .gitignore.
Once you finished with that, the will create the Flask SocketIO the following project's structure:

example-project
|  
|---app  
|&nbsp;&nbsp;&nbsp;&nbsp;|  ---   \_\_init\_\_.py  
|  
|---static  
|&nbsp;&nbsp;&nbsp;&nbsp;|  ---   css  
|&nbsp;&nbsp;&nbsp;&nbsp;|  ---   img  
|&nbsp;&nbsp;&nbsp;&nbsp;|  ---   js  
|  
|---templates  
|&nbsp;&nbsp;&nbsp;&nbsp;|  ---   index.html  
|  
|---tests  
|&nbsp;&nbsp;&nbsp;&nbsp;|  ---   app  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  ---   \_\_init\_\_.py  
|&nbsp;&nbsp;&nbsp;&nbsp;|  ---   \_\_init\_\_.py  
|  
|---   .gitignore  
|---   docker-compose.yaml  
|---   Dockerfile  
|---   main.py  
|---   README.MD  
|---   requirements.txt  

Once the project was generated execute **docker-compose up** from your project's root. You can access the Flask application on *localhost:5000*.

## Contributing
If you'd like to contribute to Flask-SocketIO-Generator, feel free to fork the repository, submit issues, or create pull requests. Contributions are always welcome!
