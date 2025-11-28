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

print(f"my_list = {my_list}")
while (my_list):
    del my_list[-1]
    print(f"my_list = {my_list}")
