def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    previous_hand = {}

    while True:
        user_input = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if user_input == 'e':
            break

        elif user_input == 'n':
            hand = dealHand(HAND_SIZE)
            previous_hand = hand

        elif user_input == 'r':
            if not previous_hand:
                print("You have not played a hand yet. Please play a new hand first!")
                continue

        else:
            print("Invalid command.")
            continue

        while True:
            opponent_choice = input("Enter u to have yourself play, c to have the computer play: ")

            if opponent_choice in ['u', 'c']:
                break
            else:
                print("Invalid command.")

        if opponent_choice == 'u':
            if user_input == 'n' or (user_input == 'r' and previous_hand):
                playHand(previous_hand, wordList, HAND_SIZE)

        elif opponent_choice == 'c':
            if user_input == 'n' or (user_input == 'r' and previous_hand):
                compPlayHand(previous_hand, wordList, HAND_SIZE)

