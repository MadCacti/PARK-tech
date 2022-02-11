import random

hang = ["""
HANGMAN

   +---+
   |   |
       |
       |
       |
       |
_______=""", """
HANGMAN

  +---+
  |   |
  O   |
      |
      |
      |
______=""", """
HANGMAN

  +---+
  |   |
  O   |
  |   |
      |
      |
______=""", """
HANGMAN

  +---+
  |   |
  O   |
 /|   |
      |
      |
______=""", """
HANGMAN

  +---+
  |   |
  O   |
 /|\  |
      |
      |
______=""", """
HANGMAN

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
______=""", """
HANGMAN

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
______="""]


def getRandomWord():
    words = ['great gatsby', 'harry potter', 'animal farm', 'cat in the hat', 'romeo and juliet']

    word = random.choice(words)
    return word
def getRandomAuthor():
    authors = ['stephen king', 'jk rowling', 'george orwell', 'mark twain', 'william shakespeare', 'roald dahl', 'rick riordan', 'dr seuss']

def displayBoard(hang, missedLetters, correctLetters, book):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(book)

    for i in range(len(book)):  # replace blanks with correctly guessed letters
        if book[i] in correctLetters:
            blanks = blanks[:i] + book[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in '  abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    return input("\nDo you want to play again? ").lower().startswith('y')


missedLetters = ''
correctLetters = ''
book = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, book)

    guess = getGuess(missedLetters + correctLetters)

    if guess in book:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(book)):
            if book[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The book is "' +
                  book + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, book)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the book was "' + book + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            book = getRandomWord()
        else:
            break