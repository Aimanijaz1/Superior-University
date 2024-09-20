#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# HangMan
import random

words = ["sunflower", "python", "hello", "world", "algorithms", "programming"]
class Hangman:
    hangman_stages = [
        """
         ------
         |    |
              |
              |
              |
              |
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\   |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\   |
        /     |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\   |
        / \   |
              |
        """
    ]


    def __init__(self):
        self.word = random.choice(words)
        self.display = ["_" for letter in self.word]
        self.guesses = 0
        self.lives = 6

    def show(self):
        display = "_". join(self.display)
        print(f"The word is: {display}")
        print(self.hangman_stages[6 - self.lives])

    def get_word_index(self, guess):
        locations = []
        for index, char in enumerate(list(self.word)):
            if char == guess:
                locations.append(index)
        return locations
    
    def update(self, index, letter):
        for number in index:
            self.display[number] = letter

    def check_guess(self, guess):
        if guess in self.word:
            index = self.get_word_index(guess)
            self.update(index, guess)
        else:
            self.lives -= 1

    def check_for_win(self):
        display =''.join(self.display)
        word = self.word
        if display == word:
            print("You Win!!!")
            return True
    
def game():
    active = True
    hangman = Hangman()
    while True:
        if hangman.lives <= 0:
            print("You lost! The Word was: ", hangman.word)
            break
        guess = input("Guess a letter>>>").lower()
        hangman.check_guess(guess)
        hangman.show()
        hangman.guesses += 1
        if hangman.check_for_win():
            print(f"You won in {hangman.guesses} guesses!")
            break
def loop():
    while True:
        response = input("DO you want to play HangMan!!")
        if response == "no":
            break
        game()
loop()


# In[ ]:




