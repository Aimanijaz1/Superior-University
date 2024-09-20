#!/usr/bin/env python
# coding: utf-8

# In[89]:


class LuhnAlgorithm:
    def __init__(self, card_number):
        # Convert the card number into a list of integers
        self.card_number = [int(digit) for digit in card_number]
        # Step 1: Remove the rightmost digit (checking digit)
        self.checking_digit = self.card_number.pop()
        # Step 2: Reverse the order of the remaining digits
        self.card_number.reverse()

    def double_even_indices(self):
        # Step 3: Double the digits at even indices
        for i in range(len(self.card_number)):
            if i % 2 == 0:  # Check if index is even
                self.card_number[i] *= 2
                # Step 4: If any results are greater than 9, subtract 9 from those
                if self.card_number[i] > 9:
                    self.card_number[i] -= 9

    def calculate_total(self):
        # Step 5: Add all together including the checking digit
        total_sum = sum(self.card_number) + self.checking_digit
        return total_sum

    def validate_card_number(self):
        # Step 6: Check if total is divisible by 10
        total = self.calculate_total()
        return total % 10 == 0

card_number = input("Enter your card number: ")
luhn_obj = LuhnAlgorithm(card_number)
luhn_obj.double_even_indices()

if luhn_obj.validate_card_number():
    print("The card number is valid.")
else:
    print("The card number is invalid.")

Question 02
# In[67]:


punctuations = '''!()-[]{};:'"|\,<>./?@#$%^&*_~`'''
User_input = input("Enter your String: ")
no_punct = ""
for char in User_input:
    if char not in punctuations:
        no_punct = no_punct + char
print("String After removing punctuations: ")        
print(no_punct)


# In[90]:


word = "word"

# Convert the input into a list of characters
char_list = list(word)

# Bubble sort to sort in alphabetical order
for j in range(len(char_list) - 1):
    for k in range(len(char_list) - 1 - j):
        if char_list[k] > char_list[k + 1]:
            # Swap if the current character is greater than the next
            char_list[k], char_list[k + 1] = char_list[k + 1], char_list[k]

# Join the sorted list back into a string
sorted_word = ''.join(char_list)

print("Sorted word:", sorted_word)


# In[ ]:




