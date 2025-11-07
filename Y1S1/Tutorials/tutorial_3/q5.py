#Variable Declaration
secret_num = 50
correct = 0
attempts = 0

#While Loop
while (not correct):
    num = int(input("Guess the secret number: "))
    attempts += 1
    if (num == secret_num):
        correct = 1
    else:
        if (num < secret_num):
            print("Guess is too low")
        else:
            print("Guess is too high")

#Message printed when user guesses correctly
print(f"Well done, You took {attempts} attempts.")
