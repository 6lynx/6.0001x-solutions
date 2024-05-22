def getGuessedWord(secretWord, lettersGuessed):
    result = ['_'] * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            result[i] = secretWord[i]

    return ' '.join(result)