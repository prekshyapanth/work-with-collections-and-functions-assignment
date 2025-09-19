#Part 1: Tuples
#1. Create and Access
#a. Define a tuple with at least 5 numerical values.
 #"""Tuple in python is an ordered and mutable collection of the elements.
# Once the tuple is created, its elements cannot be changed, added or removed.


numerical_values= (5,6,8.5,26,100)
print(type(numerical_values))

#b. Print the third item in the tuple.
print(numerical_values[2])

#2. Tuple Modification (Workaround)

#a. Since tuples are immutable, demonstrate how to remove an item by converting the tuple to a list, removing an item, and converting it back.

numerical_values= (5,6,8.5,26, 100) #tuples
numerical= list(numerical_values) #convert tuple to list
numerical.remove(26) #remove an item from list
print(numerical) #print numerical
num= tuple(numerical) #converts list to tuple
print(num)

#3. Tuple Unpacking

#a. Unpack a tuple into individual variables and print each variable.

unpack_tuple= ("prekshya", 30, 1993)
a,b,c= unpack_tuple

print(f"name: {a}, age: {b}, date of year:{c}")

#4. Tuple to String

#a. Convert a tuple of characters into a single string and print it.
a= ("My", "name", "is", "Prekshya") #tuple of charcters
b= "".join(a)
print(b)


#5.Find Duplicates

# a. Given a tuple with repeated elements, identify and print the duplicate values.

duplicate_elements= ("Apple", "Banana", "Cherry", "Dragon Fruit", "Apple")
duplicates=[]
for i in duplicate_elements:
    if i > str(duplicate_elements):
        duplicates.append(i)
print(f"Duplicate values in the tuple is : {i}")

#6. Reverse Tuple

#a. Print the tuple in reverse order using slicing.
reverse = ("a", "b", "c","d","e")
b= reverse[::-1]
print(b)


# Part 2:
#7. Sum of List
#a. Write code to sum all the items in a list of numbers.
numbers= [20,30,40,50]
b= sum(numbers)
print(b)

#Remove Duplicates

#a. Remove duplicate values from a list while maintaining the original order.

numbers= [1,2,3,4,5,6,2,3,6]
count= []

for i in numbers:
    if i not in count:
        count.append(i)
print(count)

#9. Clone a List

#a. Show three different ways to copy a list.

clone_list=[1,2,3,4,5,6,7,8,9,10]
clone_a_list= clone_list.copy()
print(clone_a_list)

clone_list_1=[1,2,3,4,5,6,7,8,9,10,11]
clone_a_list_1= clone_list_1[:]
print(clone_a_list_1)

clone_list_2= [1,2,3,4,5,6,7,8,9,10,11,12]
clone_list_2= list(clone_list_2)
print(clone_list_2)

#10. Combine Lists

#a. Create two separate lists and append one to the other. Print the combined result.

list_1= ["prekshya", "panth", "ayush", "dangol"]
list_2= ["nancy","shrestha", "prakash","shrestha"]
list_1.extend(list_2)
print(list_1)

#11. Sort by Last Element in Tuple

#a. Given a list of non-empty tuples, sort the list in increasing order based on the last element of each tuple.
non_empty_tuple= ["Apple", "Banana", "Cherry", "Dragonfruit","Eggplant"]
non_empty_tuple.sort(reverse=True)
print(non_empty_tuple)


#12. List Slicing
#a. Create a list with names of 10 people. Use slicing to print the first 4 names.
list_names= ["Prekshya", "Ayush", "Prasiddha","Manon","Saisha", "Sparsh","Barsha", "Mythali", "Rakshya", "Aarzoo"]
print(list_names[:4])

#Part 3: Sets
#13. Create a Set

#a. Create a set of at least 5 elements and print it.

a= {1,2,3,4,5}
print(a)

#14. Set Intersection

#a. Create two sets with some common elements. Find and print their intersection.

one_set= {1,2,3,4,5}
two_set= {4,5,6,7,8}

intersection_result= one_set.intersection(two_set)
print(intersection_result)

#15. 15. Set Union

#a. Print the union of the same two sets.

union_result= one_set.union(two_set)
print(union_result)


#Part 4: Functions
#16. Multiply List Elements

# a. Define a function that takes a list of numbers and returns the product of all numbers.


def list_numbers(numbers):  #define function with list of number
    product = 1
    for n in numbers:
        product *= n
    return product

print(list_numbers([2,3,4,5,5]))


#17. Statistics Function

#a. Generate a list of test scores.
#b. Write a function that returns the minimum, maximum, and average of the list.

def test_scores(scores):
    test= 1
    for result in scores:
        print (result)



test_scores([min(85.5,26.2,15)])
test_scores([max(85.5,26.2,15)])
### average


#18. Check Range Membership

#a. Write a function that checks if a given number is within a specified range.

def given_number(num):
    if num in range(0,6):
        print( f"True:The given number is in range")
    else:
        print(f"False: The given number is not in range")

given_number(5)
given_number(10)


#19. Dog Speed Analyzer

#a. Create a nested list, each item containing a dog breed and its max running speed (e.g., ["Greyhound", 45]).
#b. Write a function to determine which dog breed is the fastest and which is the slowest.

