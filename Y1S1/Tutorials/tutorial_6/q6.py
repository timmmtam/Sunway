#Variable Init
my_list = []
start = True

#User input
while (start):
    data = input("Enter a data: ")
    my_list.append(data)
    add_data = input("Do you want to continue? (Y/N): ")
    add_data.lower()
    if (add_data == "y"):
        start = True
    else:
        start = False

print(f"my_list = {my_list}")
i = len(my_list) - 1
while (i >= 0):
    if (i % 2 == 0):
        del my_list[i]
        i -= 1
    print(f"my_list = {my_list}")
    i -= 1
