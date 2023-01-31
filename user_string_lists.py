"""
# Name: Kendall Outlaw
# Date: 01/29/2023
# Data Analysis Fundamentals Project 3 
# Domain: Timesheet
# Purpose : The purpose is to complete the exercises using list with strings
"""
# lists of company sections, equipment, and other attributes

department = ["Finance", "Security", "IT", "Traning", "HR"]

position = ["Database Administrator", "Maintenance Shop Supervisor", "Production Control Clerk", "Material Coordinator", "Warehouse Specialist"]

billing_type = ["Regular", "Sick Leave", "Vacation", "Leave Without Pay", "Holiday"]

equipment = ["17 inch Monitor", "HP Desktop", "HP Laptop", "HP Printer", "HP Scanner"]

parking_pass = ["Permanent Pass", "30 Day Parking Pass", "90 Day Parking Pass", "No Pass"]



"""
Use the built-in functions: len(), set(), zip() to combine 2 or more lists into tuples
"""
print("String Lists 1. Using Python Built-in Functions")

# Use len function
print(f"The length of the company departments list is {len(department)}.")

# Use set function
print(f"The set function has these unique values in the position list: {set(position)}.")

# Combine the multiple lists with zip function
company_tuples = zip(billing_type, equipment, parking_pass)
print(f"Tuples of billing_type, equipment, and parking_pass: {list(company_tuples)}")




print("String Lists 2. Random Choice")

#random choice
import random

"""
Use random.choice() to pick a random value from one of your lists.
"""

print(f"A random choice from parking pass list is : {random.choice(parking_pass)}")


"""
Customize the sentence generator to create random sentences about your domain. 
"""

randomized_sentence_generator = (
    f"This new employee will be assigned to the {random.choice(department)} and he/she will be issued a {random.choice(parking_pass)}"
    f" and be given a {random.choice(equipment)}."
)

print(randomized_sentence_generator)


print()

print("String Lists 3. Get Unique Words")


"""
1. Choose one of the text data files in the repo - or add another related your your domain.

"""

# I am choosing the text_juliuscaesar.txt from the repo

"""
2. Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
"""


with open("text_juliuscaesar.txt", "r") as file:
    text = file.read()
    list_of_words = text.split()
    unique_words = set(list_of_words)

"""
3. Sort the list
"""

sort_unique_words = sorted(unique_words)

"""
4. Use len() to get the length display it to the console.
"""

unique_word_count = len(sort_unique_words)
print(f"Julius Caesar contains {unique_word_count} unique words.")


print()

"""
5. How good is your list?
""" 
# The came out correctly