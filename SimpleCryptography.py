def decipherOptionValidation():
    option = str(input())
    while (option != "cipher" and option != "Cipher" and option != "decipher" and option != "Decipher"):
        option = str(input(print("ERROR: Invalid option. Please specify either 'cipher' or 'decipher'.\n")))
    if (option == "cipher" or option == "Cipher"):
        return "cipher"
    elif (option == "decipher" or option == "Decipher"):
        return "decipher"

def actionTypeValidation():
    aType = str(input())
    while (aType != "Atbash" and aType != "Ceaser Cypher" and aType != "ROT"):
        print("ERROR: Invalid option. Please specify either 'Atbash', 'Ceaser Cypher', or 'ROT'.")
        aType = str(input())
    if (aType == "Atbash"):
        return "Atbash"
    elif (aType == "Ceaser Cypher"):
        return "Ceaser Cypher"
    elif (aType == "ROT"):
        return "ROT"

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]
reverseAlphabet = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q",
                   "p", "o", "n", "m", "l", "k", "j", "i", "h", "g",
                   "f", "e", "d", "c", "b", "a"]
doubleAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                  "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "a", "b", "c", "d",
                  "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                  "y", "z"]

def cipherAtbash(phrase):
   
    cipheredPhrase = ""

    for i in range(len(phrase)):
        if (phrase[i].isalpha()):
            for j in range(len(alphabet)):
                if (phrase[i] == alphabet[j]):
                    cipheredPhrase += reverseAlphabet[j]
        else:
            cipheredPhrase += phrase[i]

    print("Original phrase:", phrase, "\nCiphered phrase:", cipheredPhrase)                

def cipherCC(phrase):

    rotations = int(input("How many rotations would you like? (0 - 26)\n"))

    while (rotations < 0 or rotations > 26):
        rotations = int(input("ERROR: Out of bounds. Please enter a range of 0 - 26.\n"))
    
    cipheredPhrase = ""

    for i in range(len(phrase)):
        if (phrase[i].isalpha()):
            for j in range(len(alphabet)):
                if (phrase[i] == alphabet[j]):
                    cipheredPhrase += reverseAlphabet[j - 26 + rotations]
        else:
            cipheredPhrase += phrase[i]

    print("Original phrase:", phrase, "\nCiphered phrase:", cipheredPhrase)

def cipherROT(phrase):

    rotations = int(input("How many rotations would you like? (0 - 26)\n"))

    while (rotations < 0 or rotations > 26):
        rotations = int(input("ERROR: Out of bounds. Please enter a range of 0 - 26.\n"))
    
    cipheredPhrase = ""

    for i in range(len(phrase)):
        if (phrase[i].isalpha()):
            for j in range(len(alphabet)):
                if (phrase[i] == alphabet[j]):
                    cipheredPhrase += doubleAlphabet[j - 26 + rotations]
        else:
            cipheredPhrase += phrase[i]

    print("Original phrase:", phrase, "\nCiphered phrase:", cipheredPhrase)

def decipherAtbash(phrase):
    
    decipheredPhrase = ""

    for i in range(len(phrase)):
        if (phrase[i].isalpha()):
            for j in range(len(reverseAlphabet)):
                if (phrase[i] == reverseAlphabet[j]):
                    decipheredPhrase += alphabet[j]
        else:
            decipheredPhrase += phrase[i]

    print("Original phrase:", phrase, "\nDeciphered phrase:", decipheredPhrase)

def decipherCC(phrase):

    rotations = int(input("How many rotations would you like? (0 - 26)\n"))

    while (rotations < 0 or rotations > 26):
        rotations = int(input("ERROR: Out of bounds. Please enter a range of 0 - 26.\n"))

    decipheredPhrase = ""

    for i in range(len(phrase)):
        if (phrase[i].isalpha()):
            for j in range(len(reverseAlphabet)):
                if (phrase[i] == reverseAlphabet[j]):
                    decipheredPhrase += alphabet[j - rotations]
        else:
            decipheredPhrase += phrase[i]

    print("Original phrase:", phrase, "\nDeciphered phrase:", decipheredPhrase)

def decipherROT(phrase):

    rotations = int(input("How many rotations would you like?\n"))

    while (rotations < 0 or rotations > 26):
        rotations = int(input("ERROR: Out of bounds. Please enter a range of 0 - 26.\n"))
    
    decipheredPhrase = ""

    for i in range(len(phrase)):
        if (phrase[i].isalpha()):
            for j in range(len(alphabet)):
                if (phrase[i] == doubleAlphabet[j - rotations]):
                    decipheredPhrase += alphabet[j]
        else:
            decipheredPhrase += phrase[i]

    print("Original phrase:", phrase, "\nDeciphered phrase:", decipheredPhrase)
    
def main():
    print("Would you like to 'cipher' or 'decipher' a phrase? ")
    option = decipherOptionValidation()

    print("What type of", option, "would you like to choose? ('Atbash', 'Ceaser Cypher', 'ROT')")
    aType = actionTypeValidation()

    print("Please type the phrase that you would like to", option, "in all lowercase letters and press 'Enter'.")
    phrase = str(input())

    if (option == "cipher"):
        if (aType == "Atbash"):
            cipherAtbash(phrase)
        elif (aType == "Ceaser Cypher"):
            cipherCC(phrase)
        elif (aType == "ROT"):
            cipherROT(phrase)
    elif (option == "decipher"):
        if (aType == "Atbash"):
            decipherAtbash(phrase)
        elif (aType == "Ceaser Cypher"):
            decipherCC(phrase)
        elif (aType == "ROT"):
            decipherROT(phrase)

main()
