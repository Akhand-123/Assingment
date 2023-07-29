# 4.Write a python program that takes two strings is an anagram of the other.
def check_anagram(l1,l2):
    if sorted(l1) == sorted(l2):
        return ("Both are Anagram")
    else:
        return "Not an Anagram"
mystr1 = input("Enter the first string : ").lower()
mystr2 = input("Enter the second string : ").lower()
res = check_anagram(mystr1,mystr2)
print(res)

# Output:
# Enter the first string : abcd
# Enter the second string : dcba
# Both are Anagram