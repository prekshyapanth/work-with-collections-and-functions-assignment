

# Part 1: Tuples
# 1.Create and Access
# a.Define a tuple with at least 5 numerical values.
# Tuple in python is an ordered and mutable collection of the elements.
# Once the tuple is created, its elements cannot be changed, added or removed.


numerical_values = (5, 6, 8.5, 26, 100)  # tuple with five numerical values
print(numerical_values)  # prints five numerical values

# b. Print the third item in the tuple.
print(numerical_values[2])  # this prints the third item from the tuple

# 2. Tuple Modification (Workaround)


# a.Since tuples are immutable, demonstrate how to remove an item by converting the tuple to a list, removing an item, and converting it back.

numerical_values = (5, 6, 8.5, 26, 100)  # tuples values are stored in a varible
numerical = list(numerical_values)  # convert tuple to list
numerical.remove(26)  # removes an item from list
print(numerical)  # print list of values
num = tuple(numerical)  # converts list to tuple
print(num) # prints tuple value

# 3. Tuple Unpacking
# a. Unpack a tuple into individual variables and print each variable.

unpack_tuple = ("prekshya", 30, 1993)  # three elements in a tuple
a, b, c = unpack_tuple  # three tuples are swaped into individual variables

print(f"name: {a}, age: {b}, date of year:{c}")  # prints each variables in a tuple

# 4. Tuple to String

# a. Convert a tuple of characters into a single string and print it.
a = ("My", "name", "is", "Prekshya")  # tuple elements are stored in a variable
b = "".join(a) # takes element from a and concatenate with the string
print(b) # prints the single string characters

# 5.Find Duplicates

# a. Given a tuple with repeated elements, identify and print the duplicate values.

duplicate_elements = ("Apple", "Banana", "Cherry", "Dragon Fruit", "Apple")  # duplicate values are stored in a variable
duplicates = [] # initializes duplicate elements in form of list
for i in duplicate_elements: # loops through the tuple elements
    if duplicate_elements.count(i) > 1 and i not in duplicates:  # checks for the condition if i element and i is not duplicate
        duplicates.append(i) # adds the duplicate value
print(f"Duplicate values in the tuple is : {duplicates}") # prints the duplicate value form the tuple

# 6. Reverse Tuple
# a . Print the tuple in reverse order using slicing.
reverse = ("a", "b", "c", "d", "e") # tuple elements are stored in a variable
b = reverse[::-1] # reverse function is used with slicing -1 that prints numbers from back
print(b) # prints the reverse order

# Part 2:
# 7. Sum of List
# a . Write code to sum all the items in a list of numbers.
numbers = [20, 30, 40, 50]     # list of  number stored in variable numbers
b = sum(numbers)   # finds the sum of the numbers
print(b)    # prints sum of numbers

# Remove Duplicates

# a. Remove duplicate values from a list while maintaining the original order.

numbers = [1, 2, 3, 4, 5, 6, 2, 3, 6] # duplicate numbers stored in list and has duplicate values
count = []  # initialized empty list to store unique value with list

for i in numbers: # loops through the numbers
    if i not in count: # checks weather numbers is not  in the empty variable
        count.append(i) # counts and adds number
print(count) # prints counts of number that removes duplicates value

# 9. Clone a List

# a. Show three different ways to copy a list.

clone_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # stores list of variables
clone_a_list = clone_list.copy() # .copy is used for copying a list
print(clone_a_list) # prints the copied list

clone_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # stores list of variables
clone_a_list_1 = clone_list_1[:] # slicing [:] helps to copy the variable
print(clone_a_list_1) # prints the copied list

clone_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # stores list of variables
clone_list_2 = list(clone_list_2) # creating new variable and storing list with the previous variable copies
print(clone_list_2) # prints the copied list

# 10. Combine Lists

# a. Create two separate lists and append one to the other. Print the combined result.

list_1 = ["prekshya", "panth", "ayush", "dangol"]  # creates list of elements
list_2 = ["nancy", "shrestha", "prakash", "shrestha"] #creates another list of elements
list_1.extend(list_2) # extends function helps to append list of elements
print(list_1) # prints list of appended elements

# 11. Sort by Last Element in Tuple

# a. Given a list of non-empty tuples, sort the list in increasing order based on the last element of each tuple.
non_empty_tuple = [("Apple", "Banana", "Cherry", "Dragonfruit", "Eggplant")] # creates list of elements
non_empty_tuple.sort(key= lambda x: x [-1]) # checks the lambda function from backwards and sorts to a varaible
print(non_empty_tuple) #prints the sorted list

#12. List Slicing
#a. Create a list with names of 10 people. Use slicing to print the first 4 names.
list_names = ["Prekshya", "Ayush", "Prasiddha", "Manon", "Saisha", "Sparsh", "Barsha", "Mythali", "Rakshya", "Aarzoo"]  # list of elements with ten people name
print(list_names[:4]) #prints last four name from the list

#Part 3: Sets
#13. Create a Set

# a. Create a set of at least 5 elements and print it.

a = {1, 2, 3, 4, 5} # the variable creates  with set elements
print(a) # prints the set elements

# 14. Set Intersection

# a. Create two sets with some common elements. Find and print their intersection.

one_set = {1, 2, 3, 4, 5}  # variable one_set creates set of elements
two_set = {4, 5, 6, 7, 8} # variable two_Set  creates set of elements
intersection_result = one_set.intersection(two_set)  # .intersect function is useful for finding the common elements
print(intersection_result) # prints the common elements

# 15. 15. Set Union

# a. Print the union of the same two sets.

union_result = one_set.union(two_set) # .union function is used to find the union of two sets
print(union_result) # prints union of two sets


#Part 4: Functions
#16. Multiply List Elements

# a. Define a function that takes a list of numbers and returns the product of all numbers.
def list_numbers(numbers):  # define  function with parameters
    product = 1 # initialize  product  with 1
    for n in numbers: # loops through the numbers
        product *= n # calculates product= product * numbers
    return product # return final product value


print(list_numbers([2, 3, 4, 5, 5])) # print statement is used to print product of the numbers


# 17. Statistics Function
# a. Generate a list of test scores.
scores= [85.5, 26.2, 15]
# b. Write a function that returns the minimum, maximum, and average of the list.
def test_scores(scores):   # defines function with the parameter
    minimum= min(scores) #calculates the min scores
    maximum= max(scores) #calculates the max scores
    average= sum(scores)/ len(scores) #calculates the average scores
    return minimum, maximum, average #returns the minimum, maxium and averages

print(test_scores(scores)) #prints all the maximum, minimum and average score



# 18. Check Range Membership
# a . Write a function that checks if a given number is within a specified range.

def given_number(num):       # defines function with name with the parameters
    if num in range(0, 6): # checks if the number is in range 0, 5
        print(f"True:The given number is in range") # if number is in the given range prints True
    else:
        print(f"False: The given number is not in range") # if number is not in the given range prints False


given_number(5) # this statements prints the given number is True
given_number(10) # this statement prints the given number is False

# 19. Dog Speed Analyzer

# a. Create a nested list, each item containing a dog breed and its max running speed (e.g., ["Greyhound", 45]).

dog_breed = [['Greyhound', 45], ['German Shepherd', 20], ['Husky', 35]] # nested list are stored in a variable with dog breed name and running speed
print(dog_breed) # prints the dog breed

# b. Write a function to determine which dog breed is the fastest and which is the slowest.

def dogs_breed(): # define function with the function name
    dog_breed = [['Greyhound', 45], ['German Shepherd', 20], ['Husky', 35]] # list element are kept in nested list is used to define the type of dog breed with the speed

    fastest_dog = max(dog_breed, key=lambda x: x[1]) # this line calculates max number of running speed of a dog with lambda function
    slowest_dog = min(dog_breed, key=lambda x: x[1]) # this line calculates min+ number of running speed of a dog with lambda function
    return fastest_dog, slowest_dog #return max of the fastest dog and min of the slowest dog
print(dogs_breed()) #prints the result


