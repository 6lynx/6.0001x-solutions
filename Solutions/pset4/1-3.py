def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_copy = hand.copy()

    if word not in wordList:
        return False
    
    for letter in word:
        if letter in hand_copy and hand_copy[letter] > 0:
            hand_copy[letter] -= 1
        else:
            return False

    return True
    