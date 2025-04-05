# Initialize environment
pipenv --python 3.9

# Install production package
pipenv install requests

# Install dev dependency
pipenv install --dev pylint

# Run script in environment
pipenv run python main.py

# Generate lock file
pipenv lock