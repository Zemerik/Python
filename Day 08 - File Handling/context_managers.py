# Using with statement (recommended)
with open("diary.txt", "w") as file:
    file.write("2023-07-20: Learned file handling!\n")
    file.write("2023-07-21: Built a file organizer\n")

# Reading lines
with open("diary.txt", "r") as file:
    lines = file.readlines()
    print("Journal entries:", len(lines))