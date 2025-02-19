template = """# Python bytecode files
__pycache__/
*.pyc
*.pyo
*.pyd
*.pdb

# Virtual Environment
venv/
env/
ENV/
venv.bak/
env.bak/

# Flask instance folder (for development)
instance/

# Flask application logs
*.log

# Local configuration files
*.env
*.ini

# PyCharm IDE files
.idea/

# VS Code files
.vscode/

# MacOS system files
.DS_Store

# Windows system files
Thumbs.db

# Docker files
*.dockerfile

# Node.js related (if you're using frontend assets with npm or yarn)
node_modules/

# Coverage reports (if using pytest or coverage tools)
.coverage
.coverage.*

# Pytest cache
.pytest_cache
.cache/

# SQLite database file (if using SQLite as database)
*.sqlite3
*.db

# Sphinx documentation (if generated)
_docs/

# Files related to IDEs or editors
*.sublime-project
*.sublime-workspace
*.swp

# Gunicorn logs
gunicorn.log

# Environment files (if you are using dotenv or other configuration systems)
.env
"""
