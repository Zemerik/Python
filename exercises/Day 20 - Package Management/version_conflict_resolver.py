"""
Exercise 2: Version Conflict Resolver
Resolve a simulated version conflict:
- Package A requires libX>=2.0
- Package B requires libX<2.0
- Find compatible versions and explain the result
"""

class VersionConflictResolver:
    """Simulate resolving a version conflict between dependencies"""
    
    def resolve_conflict(self):
        print("=== Version Conflict Resolver ===")
        print("Package A requires: libX>=2.0")
        print("Package B requires: libX<2.0")
        print("\nChecking for compatible versions...")
        # Simulate available versions
        available_versions = ["1.8", "1.9", "2.0", "2.1", "2.2"]
        compatible = [v for v in available_versions if float(v) >= 2.0 and float(v) < 2.0]
        if compatible:
            print(f"Compatible version(s) found: {compatible}")
        else:
            print("No compatible version exists. This is a true conflict.")
            print("You must either:")
            print("- Upgrade Package B to support libX>=2.0, or")
            print("- Downgrade Package A to support libX<2.0, or")
            print("- Find alternative packages.")

def main():
    resolver = VersionConflictResolver()
    resolver.resolve_conflict()

if __name__ == "__main__":
    main() 