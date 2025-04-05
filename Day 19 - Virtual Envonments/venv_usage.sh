# Create virtual environment
python -m venv my_project_env

# Activate (Unix/macOS)
source my_project_env/bin/activate

# Install packages
pip install -r requirements.txt

# Freeze dependencies
pip freeze > requirements.txt

# Deactivate
deactivate