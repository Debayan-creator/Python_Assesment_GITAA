'''
Day 3
'''
'''
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
'''

first = "Thirty"
second = "Days"
third = "Of"
fourth = "Python"

combined = first+" "+second+" "+third+" "+ fourth
print(combined)

'''
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) 
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
'''

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())

print(company.title())

print(company.swapcase())

print(company[0:6])

print(company.find('Coding'))

print(company.replace("Coding","Python"))

print(company.split())

x=company.split()
y=[word[0].upper() for word in x]
acr=''.join(y)
print("Acronym ",acr)

position = company.index("C")
print(position)


'''
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
'''
new = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(new.split(','))

'''
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''

company = "You cannot end a sentence with because because because is a conjunction"

position = company.index("because")
print("First position", position)

position = company.rindex("because")
print("last position", position)

phrase_to_remove = 'because because because ' 
new_sentence = company.replace(phrase_to_remove, '')
print(new_sentence)

'''
Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
'''

company="Coding for All"

print(company.startswith("Coding"))
print(company.endswith("coding"))

company = "   Coding For All      "

print(company.replace("   ",""))

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

company=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(" # ".join(company))

'''
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

