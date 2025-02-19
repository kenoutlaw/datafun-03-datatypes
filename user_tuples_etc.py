"""
# Name: Kendall Outlaw
# Date: 01/29/2023
# Data Analysis Fundamentals Project 3 
# Domain: Timesheet
# Purpose: The purpose is to complete the exercises using tuples, sets, and dictionaries 

"""


"""
4. Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples.
"""


# Tuples
Week_One_Hours = (8, 7, 9, 10, 7)
Week_Two_Hours = (6, 8, 10, 11, 9)
Week_Three_Hours = (7, 11, 6, 10, 11)
Week_Four_Hours = (10, 11, 8, 8, 9)


print(f"Employee Hours for Week 1: {Week_One_Hours}")
print(f"Employee Hours for Week 2: {Week_Two_Hours}")
print(f"Employee Hours for Week 3: {Week_Three_Hours}")
print(f"Employee Hours for Week 4: {Week_Four_Hours}")



# Create some tuples
Week_One_Hours = (1, 5, 3, 4, 2)
Week_Two_Hours = (7, 9, 6, 8, 11)

# tuple concatenation
Week_One_and_Two_Hours  = Week_One_Hours + Week_Two_Hours


# tuple repetition
Week_Three_Thrice = Week_Three_Hours * 3



# tuple indexing (0 is first, -1 is last, or 1 less than the length)
Week_Four_Hours = (10, 11, 8, 8, 9)
first = Week_Four_Hours[0]
second = Week_Four_Hours[1]
third = Week_Four_Hours[2]
last = Week_Four_Hours[-1]


# Slice tuples
Week_One_Slice  = Week_One_Hours[:2]
Week_Two_Slice = Week_Two_Hours[4:]
Week_Three_Slice  = Week_Three_Hours[:3]
Week_Four_Slice = Week_Two_Hours[1:]

print(f"Week 1 Slice: {Week_One_Slice}")
print(f"Week 2 Slice: {Week_Two_Slice}")
print(f"Week 3 Slice: {Week_Three_Slice}")
print(f"Week 4 Slice: {Week_Four_Slice}")



print()

"""
5. Sets: create two sets. Get the intersection and the union.
"""

set1 = {"Morning shift", "Midday shift", "Afternoon shift", "Evening shift"}
set2 = {"Permanent Pass", "30 Day Parking Pass", "90 Day Parking Pass", "No Pass"}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

set_of_intersection = set1 & set2
print(f"The intersection of sets 1 and 2 is: {set_of_intersection}")

set_of_union = set1 | set2
print(f"The union of sets 1 and 2 is: {set_of_union}")




print()

"""
6. Dictionaries: See the examples. 
"""


"""
7. Use a dictionary to create key-value pairs of each word and its count from a file. 
"""


# I am choosing the text_zen_of_python.txt from the repo

with open("text_zen_of_python.txt") as text:
    word_list = text.read().split()

word_counts_dict = {word: word_list.count(word) for word in word_list}
print(f"Word Counts in Zen Python Text: {word_counts_dict}")



print()

"""
8. See the example file. Using a loop is okay, but the true Python approach is a dictionary comprehension (fully defining how to build a dict from a list in one short line of code. 

"""
