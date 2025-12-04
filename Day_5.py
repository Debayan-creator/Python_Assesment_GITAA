'''
Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

'''

empty_list = []
List = ['ABC', 'DEF', '56', 'ED', 65]

size = len(List)
print(size)

print(List[0], List[int((size+0)/2)], List[size-1])

'''
Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list
'''


it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

size = len(it_companies)

print("First: {}, Second: {}, Third: {}".format(
    it_companies[0],
    it_companies[int(size/2)],
    it_companies[size-1]
))

print("After modification")
it_companies[0]="GITAA"
print(it_companies)

it_companies.append("TATA")
print("After adding new")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

print(" # ".join(it_companies))

it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

for x in it_companies:
    if x=="Amazon":
        print("Yes it exist")

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print("Slicing the first 3",it_companies[3:size])

del it_companies
print(it_companies)


'''
Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print("After Joining ",front_end)

full_stack = front_end
print("New varible ",full_stack)

print(full_stack.index("Redux"))

full_stack[5:5]=["Python","Sql"]
print("Adding new ele after Redux",full_stack)

'''
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
'''


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic_countries = countries

print(first)
print(second)
print(third)
print(scandic_countries)




