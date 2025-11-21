run = input("Run the program? (Y/N): ")

while (run.upper() == "Y"):
    #Temperature Conversion Program
    print("Temperature Conversion Programme.\n[1]Celcius to Fahrenheit\n[2]Fahrenheit to Celcius")

    #Variable Init
    f_to_c = int(input("Choose [1] or [2]: "))

    #Conversion Selector
    if (f_to_c == 1):
        print ("Conversion from Fahrenheit to Celcius.")
    elif (f_to_c == 2):
        print ("Conversion from Celcius to Fahrenheit")
    else:
        print ("Error! Invalid input. Please choose [1] or [2].")
        run = input("Do you want to run the program again? (Y/N): ")
        continue

    #Min Max Input
    min_temp = int(input("Enter minimum temperature (int): "))
    max_temp = int(input("Enter maximum temperature (int): "))
    if (min_temp > max_temp):
        print("Error! Max temp is lower than min temp")
        run = input("Do you want to run the program again? (Y/N): ")
        continue

    #Conversion Display
    while (min_temp <= max_temp):
        if (f_to_c == 1):
            print (f"{min_temp}F = {(min_temp - 32) * 5 / 9:.1f}C")
        else:
            print (f"{min_temp}C = {min_temp * 9 / 5 + 32:.1f}F")
        min_temp += 1

    #Exit Message
    print("Thanks for using the program!")
    run = input("Do you want to run the program again? (Y/N): ")