print("DRINK OF THE DAY\n")
dow = int(input("Enter the day of week in numbers (1 = Monday, 2 = Tuesday, ..., 7 = Sunday): "))

match dow:
    case 1:
        print("The drink of the day today is... Peppermint Mocha!")
    case 2:
        print("The drink of the day today is... Candy Bar Latte!")
    case 3:
        print("The drink of the day today is... Caramel Coffee!")
    case 4:
        print("The drink of the day today is... Chocolate Almond Cafe Au Lait!")
    case 5:
        print("The drink of the day today is... Pumpkin-Chai Latte!")
    case 6:
        print("The drink of the day today is... Vanilla Chai Tea!")
    case 7:
        print("The drink of the day today is... Gingerbread Latte!")
    case _:
        print("Invalid day entered, please enter numbers '1-7'")
