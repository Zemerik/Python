import pkg_resources

def check_version(package, required_version):
    installed = pkg_resources.get_distribution(package).version
    print(f"{package} installed: {installed}")
    print(f"Required: {required_version}")
    return pkg_resources.parse_version(installed) >= pkg_resources.parse_version(required_version)

# Usage
if check_version("requests", "2.25.0"):
    print("Version requirements met")
else:
    print("Version mismatch!")