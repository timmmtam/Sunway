#init
num = 0
count = 0

while (count < 10):
    temp = int(input("Enter Number: "))
    if (temp > 0):
        num += temp
    count += 1

print (f"Sum of Positive Numbers: {num}")