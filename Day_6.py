'''
Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Unpack siblings and parents from family_members
'''

empty_tuple=()
sister_tuple = ('sister1','sister2','sister3')
print("Sister",sister_tuple)

brother_tuple = ('brother1','brother2','brother3')
print("Brother",brother_tuple)

siblings=sister_tuple+brother_tuple
print("Joining the two", siblings)

print("Sibling count", len(siblings) )

lst = list(siblings)
lst[6:6]=["Father","Mother"]
print(lst)

siblings=tuple(lst)

print("Modified tuple", siblings)

*rest, second_last, last = siblings

print("last",last)
print("second_last",second_last)
print("Rest",rest)


'''
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_staff_lt list
Delete the food_staff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''

fruits=('mango','apple','litchi')
veg = ('carrot', 'onion','potato')
animal = ('cow','dog','horse')

food_stuff_tp = fruits+veg+animal


fruits=('mango','apple','litchi')
veg = ('carrot', 'onion','potato')
animal = ('cow','dog','horse')

food_stuff_tp = fruits+veg+animal
print(food_stuff_tp)

food_stuff_lt=food_stuff_tp

print("After tuple variable name modifcation: ",food_stuff_lt)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

for x in nordic_countries:
    if x == "Estonia" or x == "Iceland":
        print("One exist",x)