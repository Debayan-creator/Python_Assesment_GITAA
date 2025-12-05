'''
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print("Len of set: ",len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["TATA","MAHINDRA"])
print("After adding two names once",it_companies)

it_companies.remove("TATA")
print("AFter Removing", it_companies) ## difference_update to remove multiple at once


'''
discard - no error if item missing
remove - error if item missing
'''

'''
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

print("Joining two sets: ",C)
print("Intersection: ", A.intersection(B))
print("Is Subset? ", A.issubset(B))
print("Is disjoint? ", A.isdisjoint(B))
print("Symmetric Differnce ", A.symmetric_difference(B))

del C


'''
Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''
age = [22, 19, 24, 25, 26, 24, 25, 24]

ages_set=set(age)
print("Ages as SET ",ages_set)

len_s = len(ages_set)
len_l = len(age)

if(len_s>len_l):
    print("Set is larger")
else:
    print("List is larger")

'''    
String, ordered, immutable, collection of characters.

List, ordered, mutable, allows duplicates.

Tuple, ordered, immutable, allows duplicates.

Set, unordered, mutable, unique elements only (no duplicates).
'''

string = "I am a teacher and I love to inspire and teach people"

print(string.split())


set_string = set(string)

print(set_string)

