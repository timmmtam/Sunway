#Multiplicatio Table Generator

#User Input
num = int(input("Which multiplication table would you like to generate (1-12)?: "))

#Program Output
print(f"\nMultiplication Table for {num}")
for i in range(1,13):
    print(f"{i} x {num} = {i * num}")
