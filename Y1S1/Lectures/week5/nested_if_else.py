#Input from user
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

#Calculation
if (n1 > n2 ):
    if (n1 > n3):
        print(f"Largest number is: {n1}")
    else:
        print(f"Largest number is: {n3}")
else:
    if (n2 > n3):
        print(f"Largest number is: {n2}")
    else:
        print(f"Largest number is: {n3}")