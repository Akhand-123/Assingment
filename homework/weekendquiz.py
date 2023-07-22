
# *********************************************************
# 1. Write a Python program to add ‘ing’ at the end of a given string (length should be at least 3). If the given string already ends with ‘ing’, add ‘ly’ instead. If the string length of the given string is less than 3, leave it unchanged.

# Sample String : ‘abc’
# Expected Result : ‘abcing’
# Sample String : ‘string’
# Expected Result : ‘stringly’
import re
mystr=input("Enter a string : ")
if len(mystr)>=3:
    if re.search("ing",mystr)!=None:
       a= mystr+'ly'
       print(a)
    else:
        b=mystr+"ing"
        print(b)
# *********************************************************

# 2. Write a Python program to find the first appearance of the substrings ‘not’ and ‘poor’ in a given string. If ‘not’ follows ‘poor’, replace the whole ‘not’…‘poor’ substring with ‘good’. Return the resulting string.

# Sample String : ‘The lyrics is not that poor!’
# ‘The lyrics is poor!’
# Expected Result : ‘The lyrics is good!’
# ‘The lyrics is poor!’
import re
mystr=input("Enter a string : ")
if re.search('not',mystr) and re.search('poor',mystr):
    if mystr.index('not')<mystr.index('poor'):
        
        x = mystr.replace("not","")       
        y = x.replace("poor","good")
        print(x)






# *********************************************************


# 3. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

# Sample Input: [“PHP”, “Exercises”, “Backend”]
# Output : Exercises , 9
from functools import reduce

def func(l):
    # a = list(map(lambda x:len(x),l))
    b =reduce(lambda x,y:x if x>y else y,a)
    print(a,b)
    for i in range(len(a)):
        if len(l[i])==b:
            x = [l[i],str(b)]
            y = " ,".join(x)
            # print(y)
            return y
  
l = ['PHP', "Exercises", "Backend"]
print(func(l))
# *********************************************************


# 4.Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

# Sample Input : abcd
# Output : dbca
mystr = input("Enter a string : ")
a = mystr[0:1]
b = mystr[-1:-2:-1]
x=mystr.replace(a,b)
print(x)
# *********************************************************

# 5.Write a Python program to count the occurrences of each word in a given sentence.

# Sample Input : ‘the quick brown fox jumps over the lazy dog.’
# Output : {‘the’: 2, ‘jumps’: 1, ‘brown’: 1, ‘lazy’: 1, ‘fox’: 1, ‘over’: 1, ‘quick’: 1, ‘dog.’: 1}

from collections import Counter
d ="the quick brown fox jumps over the lazy dog."
d = d.split()
x = Counter(d)
print(x)
# # Second way of solving same problem
d ="the quick brown fox jumps over the lazy dog."
b = d.split()
mydict={}
for i in b:
    mydict[i]=d.count(i)
print(mydict)
# *********************************************************

