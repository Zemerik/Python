"""
Exercise 1: Project Replicator
Create a project that:
- Installs 3 packages with specific versions
- Generates requirements.txt automatically
- Replicates environment on another machine (simulate with print)
"""

class ProjectReplicator:
    """Simulate package installation and environment replication"""
    
    def __init__(self):
        self.packages = [
            ("requests", "2.32.2"),
            ("numpy", "1.21.2"),
            ("pandas", "1.3.5")
        ]
    
    def install_packages(self):
        print("=== Installing Packages ===")
        for pkg, ver in self.packages:
            print(f"pip install {pkg}=={ver}")
    
    def generate_requirements(self):
        print("\n=== Generating requirements.txt ===")
        for pkg, ver in self.packages:
            print(f"{pkg}=={ver}")
    
    def replicate_on_another_machine(self):
        print("\n=== Replicating Environment on Another Machine ===")
        print("# Copy requirements.txt to new machine")
        print("pip install -r requirements.txt")
    
    def run(self):
        self.install_packages()
        self.generate_requirements()
        self.replicate_on_another_machine()

def main():
    print("=== Project Replicator ===")
    replicator = ProjectReplicator()
    replicator.run()

if __name__ == "__main__":
    main() 