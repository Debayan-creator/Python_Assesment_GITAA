'''
Exercise-Level 1

Q1-13 naming of variables and assiging values to it

'''
first = 60
last = 89
name = "Deb"
year = 2025
is_marries=0
is_true=True
x,y,z = 4,5,6
print(x,y,z)


print("<------End of Exercise, level_1 ----->")

'''
Excersie-Level 2
'''

#Check the data type of all your variables using type() built-in function
print(type(first))
print(type(name))
print(type(is_true))

'''
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
'''

num_one = 459
num_two = 8

add = num_one+num_two
sub = num_one-num_two
mul = num_one*num_two
div = num_one/num_two
mod = num_one%num_two
power = num_one**num_two
floor = num_one//num_two

print("addition",add)
print("subtration",sub)
print("Multy",mul)
print("division",div)
print("modulos",mod)
print("power",power)
print("Floor",floor)

'''
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
'''

import math
radius = 30
pi_value = math.pi
area = pi_value*radius**2
print("Area",area)

circumference = 2*pi_value*radius
print("circumference", circumference)

custom_r = int(input("Enter radius: "))
area = pi_value*custom_r**2
print("Area",area)


'''
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
'''

first_name=input("Enter your First Name ")
second_name = input("Enter your second name ")
country=input("Enter your country name ")
age=input("Enter your age ")

print("Your name is "+first_name+" "+second_name+" of age "+age+" from "+country)

help('keywords')












