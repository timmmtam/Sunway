#Prints the first 100 prime numbers

#Variable Init
num = 3
number_count = 0

print("2")

while (number_count <= 98):
    is_prime = True
    for divisor in range(2,num):
        if (num % divisor == 0):
            is_prime = False
            break
    if (is_prime):
        print(num)
        number_count += 1
    num += 1
