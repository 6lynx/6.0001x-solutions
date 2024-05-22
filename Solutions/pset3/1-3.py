def getAvailableLetters(lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in alphabet:
        if letter not in lettersGuessed:
            result = result + letter


    return result 