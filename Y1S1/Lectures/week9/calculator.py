#Introduction
print("---Calculator---")

#Variable Init
num_list = []
result = 0

#User Input
for i in range(2):
    while (True):
        try:
            num = float(input(f"Enter number {i + 1}: "))
            num_list.append(num)
            break
        except ValueError:
            print("Error, the input is not a number. Try again.")


while (True):
    operation = input("Which operation do you want to perform (+, -, *, /) ?: ")
    if (operation == "+" or operation == "-" or operation == "*" or operation == "/"):
        break
    else:
        print("Error, the input is not an operator (+, -, *, /). Try again.")

match operation:
    case "+":
        result = num_list[0] + num_list[1]
    case "-":
        result = num_list[0] - num_list[1]
    case "*":
        result = num_list[0] * num_list[1]
    case "/":
        try:
            result = num_list[0] / num_list[1]
        except ZeroDivisionError:
            print("Fuck you.")
            exit(1)

print(f"Result is: {result}\nThanks for using the program!")
