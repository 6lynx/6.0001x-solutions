def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total_score = 0

    while calculateHandlen(hand) > 0:
        print("Current Hand: ",end='')
        displayHand(hand)
        user_input = input('Enter word, or a "." to indicate that you are finished: ')

        if user_input == '.':
            print("Goodbye! Total score: ",total_score, "points.")
            break
        else:
            if not isValidWord(user_input,hand,wordList):
                print("Invalid word, please try again.\n")
            else:
                turn_score = getWordScore(user_input,n)
                total_score += turn_score
                print('"',user_input,'"', ' earned ',turn_score,' points. ', 'Total: ',total_score, 'points\n')
                hand = updateHand(hand,user_input)
                if calculateHandlen(hand) == 0:
                    print("Run out of letters. Total score:  ",total_score," points.")