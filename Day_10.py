'''
Exercises: Level 1
Iterate 0 to 10 using for loop, do the same using while loop.

Iterate 10 to 0 using for loop, do the same using while loop.

Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers
'''

print("Using For")
for i in range(0,11):
    print(i)
print("Using While")
i = 0
while i<=10:
    print(i)
    i+=1
    
for i in range(1,8):
    print("#"*i)
s

for i in range(1,9):
    print("# "*8)

for i in range (0,11):
    print("{} X {} = {}".format(i,i,i*i))

lst= ['Python', 'Numpy','Pandas','Django', 'Flask']

for x in lst:
    print(x)

for i in range(0,101):
    if i%2==0:
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))


'''
Exercises: Level 2
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.
'''

sum=0
for i in range(0,101):
    sum +=i
print("Sum from 0 to 100: ", sum)

sum_e = 0
sum_o = 0
for i in range(0,101):
    if i%2==0:
        sum_e+=i
    else:
        sum_o+=i

print("Sum of Even numbers {}".format(sum_e))
print("Sum of Odd numbers {}".format(sum_o))

'''
Exercises: Level 3
Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
'''


for x in countries:
    if "land" in x:
        print(x)

lst = ['banana', 'orange', 'mango', 'lemon']

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_list = []

for i in range(len(fruits)-1, -1, -1):
    reversed_list.append(fruits[i])

print(reversed_list)

lang_set= set()
for country in country:
    for lang in country["languages"]:
        lang_set.add(lang)

print("Number of unique languages:", len(lang_set))

from collections import Counter

languages_count = Counter()

for ct in country:
    for lang in ct["languages"]:
        languages_count[lang] += 1

top_10_languages = languages_count.most_common(10)

print("\nTop 10 Most Spoken Languages:")
for lang, count in top_10_languages:
    print(lang, "=>", count, "countries")

top_10_populated = sorted(
    country, 
    key=lambda c: c["population"], 
    reverse=True
)[:10]

print("\nTop 10 Most Populated Countries:")
for ct in top_10_populated:
    print(ct["name"], "=>", ct["population"])


 