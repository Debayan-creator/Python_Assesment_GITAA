'''
Exercises: Level 1
Writ a function which generates a six digit/character random_user_id.
  print(random_user_id());
  '1ee33d'
Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
'''
import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    print(characters)
    print("\n")
    user_id = "".join(random.choice(characters) for _ in range(6))
    return user_id

print(random_user_id())

import random
import string

def random_user_id(len,size):
    characters = string.ascii_letters + string.digits
    #print(characters)
    print("\n")
    for i in range(0,size):
        user_id = "".join(random.choice(characters) for _ in range(len))
        print(user_id)

length=int(input("Enter length of random variable"))
size = int(input("Enter the number of times it should occus"))

random_user_id(length, size)

import random

def rgb_color_gen():
    max = 255
    min = 0
    a = random.randint(min, max)
    b = random.randint(min, max)
    c = random.randint(min, max)

    return a,b,c

print("rgb",rgb_color_gen())

'''
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

'''


def list_of_hexa(x):
    characters = string.ascii_letters + string.digits
    ans = "".join(random.choice(characters) for i in range(x))
    return ans

print("#",list_of_hexa(6))
print(f"#{list_of_hexa(6)}")
print("#{}".format(list_of_hexa(6)))

def generate_colors(s,d):
    output=[]
    if s == "hexa":
        characters = string.ascii_letters + string.digits
        for i in range(d):
            ans = "".join(random.choice(characters) for i in range(6))
            output.append(f"#{ans}")
    else:
        max = 255
        min = 0
        a = random.randint(min, max)
        b = random.randint(min, max)
        c = random.randint(min, max)
        for i in range(d):
            output.append(f"rgb({a},{b},{c})")
    print(output)

generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

'''
Exercises: Level 3
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.    
'''
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst


data = [3,4,6,7,8,8,9,0,0,7]
print(shuffle_list(data))

def get_numbers():
    pop_range = range(10)

    unique_numbers = random.sample(pop_range, k= 7)

    return unique_numbers


random_array = get_numbers()
print(f"Seven unique random numbers: {random_array}")

