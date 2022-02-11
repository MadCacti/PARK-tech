import random

def booktitlegame(): # subgame, treat like minigame
    guessnum = 0
    booklist = ["great gatsby", "harry potter", "animal farm", "cat in the hat", "romeo and juliet"]
    word = random.choice(booklist)
    blank = "_" * len(word)


def authorgame(): # subgame, treat like minigame
    guessnum = 0
    authorlist = ["stephen king", "jk rowling", "george orwell", "mark twain", "william shakespeare", "roald dahl", "rick riordan", "dr seuss"]
    word = random.choice(authorlist)
    blank = "_" * len(word)

def game(): # core game itself
    option = str(input("Do you want to play hangman for books(1) or hangman for authors(2)?"))
    if option == "1":
        booktitlegame()
    if option == "2":
        authorgame()
    else:
        game()


game() # initializes gameplay