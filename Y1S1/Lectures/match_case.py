#input
character = input("Enter a character to check whether it is a vowel or consonant: ")

if (len(character) == 1 and ((character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'))):
    match character:
        case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
            print(f"Character {character} is a vowel")
        case _:
            print(f"Character {character} is a consonant")
else:
    print("Input is invalid.")