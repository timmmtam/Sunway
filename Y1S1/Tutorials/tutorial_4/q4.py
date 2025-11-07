#Variable Declaration
total = 0
user_input = input("Enter a number or type 'DONE' to display total:")

while (user_input != "DONE"):
    total += int(user_input)
    user_input = input("Enter a number or type 'DONE' to display total:")

print(f"Total is: {total}")
