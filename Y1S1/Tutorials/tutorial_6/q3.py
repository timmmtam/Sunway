#Variable Init
forward_list = []
start = True

#User input
while (start):
    num = float(input("Enter a number: "))
    forward_list.append(num)
    add_number = input("Do you want to continue? (Y/N): ")
    add_number.lower()
    if (add_number == "y"):
        start = True
    else:
        start = False

forward_list.sort()
print(f"forward_list = {forward_list}")
reverse_list = forward_list
reverse_list.sort(reverse=True)
print(f"reverse_list =  {reverse_list}")
