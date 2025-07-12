# Day 19: Virtual Environments

## What You'll Learn:
- Creating isolated Python environments
- Using `venv` for environment management
- Managing dependencies with `pipenv`
- Maintaining separate development/production requirements
- Generating lock files for reproducibility

## Files:
1. `venv_usage.sh` - Basic venv commands
2. `pipenv_usage.sh` - Pipenv workflow
3. `requirements.txt` - Traditional dependencies
4. `Pipfile` - Pipenv configuration

## Exercises:
1. Create a project with venv that:
   - Installs packages from requirements.txt
   - Adds a new dependency and updates requirements
   - Runs a script using the isolated environment

2. Migrate the same project to pipenv that:
   - Separates production and dev dependencies
   - Maintains Pipfile.lock
   - Deploys with locked versions