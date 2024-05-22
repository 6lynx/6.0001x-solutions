def hangman(secretWord):
    mistakesMade = 0
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    print("-----------\n")
    lettersGuessed = []

    while mistakesMade < 8:
        print("You have", 8 - mistakesMade, "guesses left.")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter a valid letter!")
            print("The word:", getGuessedWord(secretWord, lettersGuessed))
            print("-----------\n")
            continue

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print("-----------\n")
            continue

        lettersGuessed.append(guess)

        if guess in secretWord:
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            print("-----------\n")

            if isWordGuessed(secretWord, lettersGuessed):
                print("Congratulations, you won!")
                return

        else:
            mistakesMade += 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            print("-----------\n")

    print("Sorry, you ran out of guesses. The word was", secretWord)

