"""
Exercise: Pipenv Workflow
Guide for managing Python environments and dependencies using pipenv.
- Initialize pipenv environment
- Install production and dev dependencies
- Maintain Pipfile.lock
- Deploy with locked versions
- Print commands and explanations (no actual subprocess calls)
"""

def show_pipenv_workflow():
    print("=== Pipenv Workflow ===")
    print("1. Initialize a new pipenv environment:")
    print("   pipenv --python 3.9")
    print("2. Install a production dependency (e.g., requests):")
    print("   pipenv install requests")
    print("3. Install a development dependency (e.g., pytest):")
    print("   pipenv install --dev pytest")
    print("4. List installed packages:")
    print("   pipenv graph")
    print("5. Run your script inside the environment:")
    print("   pipenv run python main.py")
    print("6. Generate or update the lock file:")
    print("   pipenv lock")
    print("7. Deploy with locked versions (on another machine):")
    print("   pipenv install --deploy --ignore-pipfile")
    print("\nPipenv will use Pipfile and Pipfile.lock to ensure reproducible installs.")
    print("\nTip: Use 'pipenv shell' to activate the environment interactively.")
    print("\nTo remove the environment:")
    print("   pipenv --rm")

def main():
    print("=== Pipenv Workflow Exercise ===")
    show_pipenv_workflow()
    print("\nFollow these steps in your terminal to practice pipenv workflow.")

if __name__ == "__main__":
    main() 