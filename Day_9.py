'''
Exercises: Level 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
'''


age = int(input("Enter your age: "))

if age>18:
    print("You are old enough to learn to drive.")
else:
    print("You need 3 more years to learn to drive.")

my_age = 23

your_age = int(input("Enter your age: "))

if your_age > my_age:
    print("You are {} years older than me".format(your_age-my_age))
elif your_age == my_age:
    print("We are of same age.")
else:
    print("You are {} years young than me".format(my_age-your_age))



'''
Exercises: Level 2
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''

score = int(input("Enter your score: "))

if score >=80 and score<=100:
    print("Grade is A")
elif score >=70 and score<=89:
    print("Grade is B")
elif score >=60 and score<=69:
    print("Grade is C")
elif score >=50 and score<=59:
    print("Grade is D")
elif score >=0 and score<=49:
    print("Grade is F")


season = input("Enter the month: ")

if season in ("September, October or November"):
    print("Autumn")

elif season in ("December, Januar, February"):
    print("Winter")
elif season in ("March, April, May"):
    print("Spring")
elif season in ("June, July, August"):
    print("Summer")

fruit = input("Enter fruit name: ")
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit in fruits:
    print("Fruit already exist")
else:
    fruits.append(fruit)
    print("Modifed list: ",fruits)


'''
Exercises: Level 3
Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.
'''

if "skills" in person:
    print("Skill exists", person["skills"])

if "Python" in person["skills"]:
    print("Python exist")

if "Node" and "React" and "MongoDB" in person["skills"]:
    print("Fullstack engineer")
    
elif "Node" and "Python" and "MongoDB" in person["skills"]:
    print("Back end enginner")
    
elif "JavaScript" and "React" in person["skills"]:
    print("Front end enginner")
else:
    print("Unknown title")

if person["is_marred"] == True and person["country"] == "Finland":
    print("Asabeneh Yetayeh lives in Finland. He is married.")








    