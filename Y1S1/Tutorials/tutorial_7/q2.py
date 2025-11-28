#Counter

#User Input
while True:
    num = int(input("Enter a number below 50: "))
    if (num < 50):
        break
    else:
        print("Error! The number is not below 50. Try again.")

#Program Output
for i in range(50,num,-1):
    print(f"Counting to {num}. {i}...")

print(f"Reached {num}.")
