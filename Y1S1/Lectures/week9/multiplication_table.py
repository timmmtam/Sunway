#Prints multiplication table from 2 to 9

for i in range(2,10):
    print(f"Multiplication Table for {i}:")
    for j in range (1,11):
        print(f"{i} x {j} = {i * j}")
    print()
