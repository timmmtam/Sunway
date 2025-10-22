#Input
character = input("Enter 'R' for rectangle or 'C' for circle to find its area: ")

if (character == 'c' or character == 'C'):
    radius = float(input("What is the radius of the circle?: "))
    area = float((radius ** 2) * 3.14159)
    print(f"The area of the circle is: {area:.3f}cm\u00b2")
elif (character == 'r' or character == 'R'):
    length = float(input("What is the length of the rectangle?: "))
    width = float(input("What is the width of the rectangle?: "))
    area = float(length * width)
    print(f"The area of the rectangle is: {area:.3f}")
else:
    print(f"Invalid input, enter either 'R' or 'C'")
