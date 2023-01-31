"""
Name: Kendall Outlaw
Date: 01/29/2023
Data Analysis Fundamentals Project 3 
Domain: Timesheet
Purpose: The purpose of this program is to get comfortable with using lists.
"""

# import math module

import math


""" 
Create list1 - a fairly long (20 or more list of numbers)
list1 is a list of number of hours being worked by an employee in a month
"""

list1 = [9, 10, 8, 8, 9, 7, 11, 10, 9, 8, 10, 11, 7, 8, 10, 9, 11, 8, 7, 10]

""" 
Create listx representing 10 integer times
listx represents 10 integer times
"""

listx = list(range(10))

"""
listy is a list of number of hours being worked by an employee in 2 weeks during the above times
"""

listy = [7, 8, 8, 8, 8, 9, 10, 10, 11, 11]



""" 
Calculate the mean, median, and mode (hint: import statistics module)
"""

# import statistics module
import statistics as stats


""" 
Below are the Employee Hours calculations for mean, median, mode, standard deviation, and variance
for list1
"""


print("List 1. List Statistics")
mean = stats.mean(list1)
median = stats.median(list1)
mode = stats.mode(list1)
st_dev = stats.stdev(list1)
variance = stats.variance(list1)

print(f"Employee Hours Mean: {round(mean, 2)}")
print(f"Employee Hours Median: {round(median, 2)}")
print(f"Employee Hours Mode: {round(mode, 2)}")
print(f"Employee Hours Standard Deviation: {round(st_dev, 2)}")
print(f"Employee Hours Variance: {round(variance, 2)}")

print()


print("Lists 2. Lists - Correlation and Prediction")
xycorrelation = stats.correlation(listx, listy)
slope, intercept = stats.linear_regression(listx, listy)
xfuture = 15
yfuture = slope * xfuture + intercept

print(f"Correlation between time and number of hours being worked by an employee: {round(xycorrelation, 2)}")
print(f"Slope of best-fit line for listx and listy: {round(slope, 2)}")
print(f"Intercept of best-fit line for listx and listy: {round(intercept, 2)}")
print(f"Predicted number of hours being worked by an employee at future time 15: {round(yfuture, 2)}")


print()

print("Lists 3. Lists - Using Python Built-in Functions")


"""
Calculate the min, max, length, sum, and average of list1
Create a set from list1, and sort list1 in both forward 
and reverse directions
"""
print()

min_number = min(list1)
max_number = max(list1)
length_number = len(list1)
sum_number = sum(list1)
avg_number = sum_number / length_number
set_number = set(list1)
ascending_sort = sorted(list1)
desending_sort = sorted(list1, reverse=True)

print(f"Minimum Number of Employee Hours: {min_number}")
print(f"Maximum Number of Employee Hours: {max_number}")
print(f"Number of Work Days in a Month: {length_number}")
print(f"Total Number of Employee Hours: {sum_number}")
print(f"Average Number of Employee Hours per Count: {round(avg_number, 2)}")
print(f"Employee Hours Count Set: {set_number}")
print(f"Employee Hours Sorted (Ascending): {ascending_sort}")
print(f"Employee Hours Sorted (Descending): {desending_sort}")


print()

"""
Make a new short list named lst and explore list methods
"""
print("List 4. List Methods")

# Create short list and call it lst

lst = [36, 58, 117, 5, 89, 37, 108, 122]


print(f"lst: {lst}")

# 1. Append a new value
lst.append(2)
print(f"Appended lst: {lst}")

# 2. Extend list with new list
lst.extend([41, 66, 27, 82, 94])
print(f"Extended lst: {lst}")

# 3. insert() at an index, insert a value
z = 14
lst.insert(3, z)

print(f"Insert the value of 14: {lst}")




# 4. Remove value 5 from list
lst.remove(5)
print(f"List items and Remove the value 5: {lst}")

# 5. Count how many times 2 appears in lst
print(f"The value 2 appears {lst.count(2)} times in lst.")



# 6. Sort lst in Ascending Order
lst.sort()
print(f"First Sorted in Ascending Order: {lst}")

# 7. Sort with reverse=True to get them in descending order
lst.sort(reverse=True)
print(f"First Sorted in Descending Order: {lst}")

# 8. Create a copy of lst
first_copy = lst.copy()
print(f"Copy of lst: {first_copy}")

# 9. Pop first item from list
first_item = lst.pop(0)
print(f"First item off of the list: {first_item}")

# 10. Pop last item from list
last_item = lst.pop(-1)
print(f"Last item off of the list: {last_item}")



print()

print("List 5. List Transformations - Using filter() and map()")

"""
Use filter and map functions on list1
"""

# = list(filter(lambda x: x % 2 == 0, list1))
list1_cuberoot = list(map(lambda x: x**3, list1))
list1_volume = list(map(lambda x: x * x * x, list1))

#print(f"The even temperatures from the list are: {list1_evens}")
print()
print(f"The cuberoot of each item in the list are: {list1_cuberoot}")
print()
print(f"The volume of a cube with a side equal to the value in list1 are {list1_volume}")


print()

print("Lists 6. List Transformations - Using List Comprehension")

"""
Practice using list comprehensions
"""


"""
Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff. 
"""

# Filter (start within square brackets) to get x (for each x in lst) if x is less than 4 or some other cutoff. 
filterlst = [x*x for x in lst if x < 4]
print(f"The Result of Filtering lst if value is less than 4 is {filterlst}")


"""
Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 
"""

# Triple each value in lst
triplelst = [item * 3 for item in lst]
print(f"Each value in lst tripled is {triplelst}")


print()



"""
Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.
"""
# Add 150 to each value in lst
Addonehundredfifteenlst = [item + 150 for item in lst]
print(f"The Result of Adding 150 to Each value in lst is {Addonehundredfifteenlst}")


print()










