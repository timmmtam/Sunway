#Prints all prime numbers between 2 and 100
for num in range(3,100):
    is_prime = True
    for divisor in range(2,num):
        if (num % divisor == 0):
            is_prime = False
    if (is_prime):
        print(num)
