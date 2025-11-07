#Variable Declaration
result = 1
i = 0
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

while (i < b):
    result = result * a
    i += 1

print(f"{a} to the power of {b} is {result}")