# Finally block example
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File doesn't exist")
finally:
    file.close() if 'file' in locals() else None
    print("Cleanup complete")