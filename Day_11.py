'''
Exercises: Level 1
Declare a function add_two_numbers. It takes two parameters and it returns a sum.
Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
Write a function called calculate_slope which return the slope of a linear equation
Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
'''

def add_two(a,b):
    return a+b
    
print("Add of two numbers ",add_two(3,5))

from math import pi

def area_circle(r):
    return pi*r*r
print("Area of circle ",area_circle(7))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(num," is Not an int")
    return total
print("Sum of the arguments", sum_all_nums(2, 3, "I"))


def season(x):
    if x in ("September, October or November"):
        print("Autumn")

    elif x in ("December, Januar, February"):
        print("Winter")
    elif x in ("March, April, May"):
        print("Spring")
    elif x in ("June, July, August"):
        print("Summer")
        
season("May")

def my_list(lst):
    for x in lst:
        print(x)

print("Printing the digits of the list: ")
my_list([1,2,3,4])

def reverse_list(arr):
    i=0
    while(i<len(arr)//2):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
        i+=1
    return arr
print("Reversing the list with loop",reverse_list([1, 2, 3, 4, 5]))
print("Reversing the list with loop",reverse_list(["A", "B", "C"]))


def add_item(name, para):
    name.append(para)
    return name

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print("Adding meat tot the list",add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print("Adding 5 to the list",add_item(numbers, 5))


def solve(x):
    sum_e, sum_o = 0, 0
    for i in range(x):
        if i % 2 == 0:
            sum_e += i
        else:
            sum_o += i
    return sum_e, sum_o

even_sum, odd_sum = solve(9)
print("Even Sum {} Odd Sum {}".format(even_sum, odd_sum))


'''
Exercises: Level 2
Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
Call your function is_empty, it takes a parameter and it checks if it is empty or not
Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
'''
def counter(a):
    c_e, c_o = 0,0
    for x in range(0,a+1):
        if x%2==0:
            c_e+=1
        else:
            c_o+=1
    return c_e,c_o
    
c_e, c_o = counter(100)

print("Even Count {} Odd Count {}".format(c_e, c_o))

def fact(x):
    ans =1
    while(x>1):
        ans = ans* x
        x-=1
    return ans
    
print("Factorial of the number ",fact(3))

def is_empty(x):
    return not x

print("Empty list ",is_empty([]))

def calculate_mean(x):
    sum = 0
    for value in x:
        sum=sum+value

    return sum/len(x)
def calculate_median(x):
    n = int(len(x)/2)
    return x[n]
print("Mean", calculate_mean([10, 20, 30, 40]))
print("Median", calculate_median([10, 20, 30, 40]))

'''
Write a function called is_prime, which checks if a number is prime.
Write a functions which checks if all items are unique in the list.
Write a function which checks if all the items of the list are of the same data type.
Write a function which check if provided variable is a valid python variable
Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''
import math

def is_prime(n):
    if n <= 1:
        return False
    x = int(n/2)
    for i in range(2, x):
        if n % i == 0:
            return False
    return True

print(is_prime(20))

import math

def is_prime(n):
    if n <= 1:
        return False
    x = int(n/2)
    for i in range(2, x):
        if n % i == 0:
            return False
    return True

print(is_prime(20))

def unique_item(x):
    seen = set()

    for item in x:
        if item in seen:
            return item
            break
        else:
            seen.add(item)

print("Duplicate exists ", unique_item([6,7,8,6,5]))

import keyword

def python_keyword(x):
    if x in keyword.kwlist:
        return True
    else:
        return False
print(python_keyword("def"))

from collections import Counter

def spoken(lst):
     language_counter = Counter()
    for item in data:
        for lang in item["languages"]:
            language_counter[lang] += 1
            
    return language_counter        
    
    
        
