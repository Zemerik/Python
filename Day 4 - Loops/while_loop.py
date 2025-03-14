# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break statement
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break