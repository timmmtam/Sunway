#Input
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

if (n1 > n2) and (n1 > n3):
    print(f"Largest number is: {n1}")
elif (n2 > n1) and (n2 > n3):
    print(f"Largest number is: {n2}")
else:
    print(f"Largest number is: {n3}")