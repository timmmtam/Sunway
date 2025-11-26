#Variable Initialization
num_list = []

#Display Message
print("Please enter 5 numbers to insert into a list.")

#Ask for input 5 times
for i in range(5):
    try:
        num_input = int(input(f"Enter number {i + 1}: "))
        num_list.append(num_input)
    except ValueError:
        print("Error! The value inputed is not a number.")
        break
else:
    print(f"Your list of numbers is: {num_list}")

print("Thanks for using the program.")
