#init
yes = 1
count = 0

#loop
while(yes):
    yes = 0
    cont = input("Do you want to continue or not ? (y/n)")
    if (cont == 'y'):
        yes = 1
        count += 1
        print(f"Count: {count}")