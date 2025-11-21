#01 Grid

#Variable Init
i = 0

while (i < 5):
    j = 0
    char = "1"
    while (j < 11):
        print(char, end="")
        if (char == "1"):
            char = "0"
        else:
            char = "1"
        j += 1
    print("")
    i += 1