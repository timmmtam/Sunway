#Multiplication Table Program

#Variable Init
index = 1

#Input
multiple = int(input("Which multiplication table would you like to print?: "))
ceiling = int(input("How high would you like it to go?: "))

#Calculation
print("Here is your multiplication table:")
while (index <= ceiling):
    print(f"{multiple} times {index} = {multiple * index}")
    index += 1