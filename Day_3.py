'''
Exercise - Day3
'''

'''
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
'''

Age= int(input("Enter your age "))
height = float(input("Enter your height "))
com = complex(input("Enter complex Number "))

print("Age ", Age)
print("Height ", height)
print("Complex ", com)

'''
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
'''

b = int(input("Enter Base: "))
h = int(input("Enter height: "))
area =int(0.5*b*h)

print("Area: ",area)

'''
Q6-7 similar to above
'''

'''
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
'''

m =2
y_intercept = (0,-2)
x_intercept = (1,0)

print("Slope of line y = 2x - 2:", m)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

x1, y1 = 2,2
x2, y2 = 6,10

slope = (y2-y1)/(x2-x1)

import math

distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
print("Slope between points:", slope)
print("Distance between points:", distance)


'''
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
'''

x=4
y = x**2+6*x+9
print("Value of eq",y)

def f(x):
	return x**2+6*x+9
	
print("Searching")
for x in range(-15, 15):
	if f(x)==0:
		ans=x
		break
print("Value of y is", ans)


'''
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
'''

print("printing length of python and dragon")
x = len("python")
y = len("dragon")

print(x,y)
if x == y:
	print("Both are equal in length")

if "on" in "python" or "on" in "dragon":
	print("on is present")
		
if "jargon" in "I hope this course is not full of jargon":
	print("jargon present")


a='10'
b=10
print(a is b)


if int(float('9.8')) == 10:
	print("same")

year = int(input("Enter number of years lived"))
sec = year*365*24*60*60
print("Seconds lived ",sec)

for x in range(1,6):
	col1 = x
	col2 = 1
	col3 = x
	col4 = x**2
	col5 = x**3
	
	print(col1,col2,col3,col4,col5)








