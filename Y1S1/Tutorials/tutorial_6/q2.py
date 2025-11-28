#Variable Init
my_list = []
start = True

#User input
while (start):
    num = float(input("Enter a number: "))
    my_list.append(num)
    add_number = input("Do you want to continue? (Y/N): ")
    add_number.lower()
    if (add_number == "y"):
        start = True
    else:
        start = False

print(f"Your list of numbers is: {my_list}")
print(f"Total = {sum(my_list)}")
print(f"Average = {sum(my_list) / len(my_list)}")
