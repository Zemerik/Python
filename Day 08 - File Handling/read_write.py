# Writing to a file
file = open("example.txt", "w")
file.write("First line\nSecond line\n")
file.close()

# Reading from a file
file = open("example.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()