def isWordGuessed(secretWord, lettersGuessed):
  secretList = list(secretWord)
  
  for letter in secretList[:]:
      if letter in lettersGuessed:
          secretList.remove(letter)

  return len(secretList) == 0