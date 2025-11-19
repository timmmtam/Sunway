#function import
from random import randint

#variable declaration
secret_num = randint(1,200)
correct = 0
attempts = 0
Continue = 1

while (Continue):
    num = int(input("Guess the integer (1-200): "))
    attempts += 1
    if (num == secret_num):
        correct = 1
        break
    else:
        if (num < secret_num):
            print("Guess is too low")
        else:
            print("Guess is too high")
    Continue = int(input("Do you want to continue? (0 for No, 1 for Yes)"))

if (correct):
    print(f"Well done, you have guessed correctly in {attempts} attempts")
else:
    print("Better luck next time!")