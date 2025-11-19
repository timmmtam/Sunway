#Nested while loops

i = 0
num = 1
while (i < 2):
    j = 0
    while(j < 4):
        print(num, end = "")
        num += 1
        j += 1
    print()
    i += 1