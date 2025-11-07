#init
num = 0
count = 0
cont = 1

while (cont):
    cont = 0
    cont += int(input("Enter Number (Press 0 to end) :"))
    if (cont):
        count += 1
    num += cont

#output
print(f"Average = {num / count}")