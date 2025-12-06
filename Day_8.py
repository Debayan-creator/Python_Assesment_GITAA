'''
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
'''

dog = {}

dog = {'name':'lucky', 'color':'golden', 'breed':'golden retriever', 'legs':'4', 'age':'3'}

print("Dog dict ",dog)

stu = {'first_name':'Debayan', 'last_name':'roy', 'gender':'M','age':'23', 'martial': 'unmarried', 'skills':'aiml, python','country':'India','city':'kolkata','address':'chakdah'}

print("Student dict {} is of length {}".format(stu,len(stu)))

print(stu['skills'])
stu['skills']=stu['skills'].split(",")
print(type(stu['skills']))

stu['skills'].append('c++')

print("After modifing skills ", stu)

key_list = list(stu.keys())
print("Keys as list ", key_list)

values_list = list(stu.values())
print("values as list ",values_list)

tuple_list = list(stu.items())
print("As tuple list ",tuple_list)

del stu['city']
print("After deleting city ", stu)

del stu





