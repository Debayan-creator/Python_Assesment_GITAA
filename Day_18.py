'''
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
'''

import re
from collections import Counter

words = re.findall(r'\b\w+\b',paragraph.lower())

print(words)

freq = Counter(words)

print("Most Freq word ",freq.most_common(1)[0])

import re
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
lst = re.findall(r'-?\d+', txt)
print(lst)
lst = [int(x) for x in lst]
#print(lst[len(lst)-1])
distance = int(lst[len(lst)-1]-lst[0])
print(distance)

'''
Exercises: Level 2
Write a pattern which identifies if a string is a valid python variable

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
'''
import re

def is_variable(x):
    return bool(re.fullmatch(r'[A-Za-z_]\w*',x))

print(is_variable('1firstname'))

'''
Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
'''

import re
from collections import Counter
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean = re.sub(r'%|#|@|\$|;|!|&', '', sentence)
print(clean)

words = re.findall(r'\b\w+\b', clean)
freq = Counter(words)
print(freq.most_common(3))
