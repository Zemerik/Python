"""
Exercise: Virtual Environment Manager
Demonstrate creating, activating, and managing virtual environments using venv and pipenv.
- Show commands for venv and pipenv
- Simulate installing packages and freezing requirements
- No actual subprocess calls (just print the commands and explain)
"""

class VirtualEnvManager:
    """Simulate virtual environment management with venv and pipenv"""
    
    def show_venv_usage(self):
        print("=== venv Usage ===")
        print("1. Create virtual environment:")
        print("   python -m venv my_project_env")
        print("2. Activate (Unix/macOS):")
        print("   source my_project_env/bin/activate")
        print("   # On Windows:")
        print("   my_project_env\\Scripts\\activate")
        print("3. Install packages:")
        print("   pip install -r requirements.txt")
        print("4. Freeze dependencies:")
        print("   pip freeze > requirements.txt")
        print("5. Deactivate:")
        print("   deactivate")
    
    def show_pipenv_usage(self):
        print("\n=== pipenv Usage ===")
        print("1. Initialize environment:")
        print("   pipenv --python 3.9")
        print("2. Install production package:")
        print("   pipenv install requests")
        print("3. Install dev dependency:")
        print("   pipenv install --dev pylint")
        print("4. Run script in environment:")
        print("   pipenv run python main.py")
        print("5. Generate lock file:")
        print("   pipenv lock")
    
    def show_requirements_example(self):
        print("\n=== Example requirements.txt ===")
        print("requests==2.32.2\nnumpy==1.21.2")
    
    def explain(self):
        print("\n=== Explanation ===")
        print("- venv is built-in and works everywhere. Activate before installing packages.")
        print("- pipenv manages dependencies and virtualenvs for you, with Pipfile and Pipfile.lock.")
        print("- Always freeze requirements for reproducibility.")

def main():
    print("=== Virtual Environment Manager ===")
    manager = VirtualEnvManager()
    manager.show_venv_usage()
    manager.show_pipenv_usage()
    manager.show_requirements_example()
    manager.explain()

if __name__ == "__main__":
    main() 