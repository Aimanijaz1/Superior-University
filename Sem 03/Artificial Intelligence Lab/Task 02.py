#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class FizzBuzz:
    def __init__(self):
        print("<<<Welcome to the FIZZ BUZZ Game!>>>")
        self.last_num = random.randint(1, 101)
        self.current_num = random.randint(1, 101)
        print(f"Starting numbers are: {self.last_num} and {self.current_num}")
    
    def number(self, user_input, num):
        if num % 3 == 0 and num % 5 == 0:
            correct_answer = "Fizz Buzz"
        elif num % 3 == 0:
            correct_answer = "Fizz"
        elif num % 5 == 0:
            correct_answer = "Buzz"
        else:
            correct_answer = str(num) 

        return user_input.lower() == correct_answer.lower(), correct_answer
    
    def play(self):
        while True:
            new_num = self.last_num + self.current_num
            print(f"Number: {new_num}")
            user_input = input("Enter your answer (Fizz/Buzz/Fizz Buzz or the number itself): ").strip()
            
            # Check answer is correct or not
            is_correct, correct_answer = self.number(user_input, new_num)
            
            if is_correct:
                print("Correct!")
                # Use last number and a new random number for generating a new number
                self.last_num = new_num
                self.current_num = random.randint(1, 101) 
                print(f"New number generated: {self.current_num}")
            else:
                print(f"Wrong Answer! The correct answer was: {correct_answer}")
                break

        print("Game Over.Try again!")

game = FizzBuzz()
game.play()


# In[55]:


class average_budget:
    def __init__(self, movies):
        self.movies = movies

    # adding new movies
    def new_movies(self):
        num_movies = int(input("Enter number of movies you want to add: "))
        for movie in range(num_movies):
            new_movies = input("Enter new movie name: ")
            new_budget = int(input("Enter new movie budget: "))
            self.movies.append((new_movies, new_budget))

    # average of budget        
    def average_budget(self):
        total_budget = sum(Budget for movie, Budget in self.movies)
        avg_budget = total_budget / len(self.movies)
        print("The average of all movies:", avg_budget)
        return avg_budget

    # high budget    
    def high_budget(self, avg_budget):
        for name, budget in self.movies:
            if budget > avg_budget:
                print(f"{name} has a budget of {budget}\n which is above the average.")

    # display method
    def display(self):
        self.new_movies()
        avg_budget = self.average_budget()
        self.high_budget(avg_budget)

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

obj = average_budget(movies)
obj.display()


# In[ ]:




