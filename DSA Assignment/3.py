# Q3. Write a program to check if two strings are a rotation of each other?
def isrotationof(string1,string2):
    if string1 == string2[::-1]:
        return True
    else:
        return False
def main():
    string1 = input("Enter a string : ").lower()
    string2 = input("Enter a string : ").lower()
    res = isrotationof(string1,string2)
    if res:
        print(f"{string1} is rotation of {string2}")
    else:
        print(f"{string1} is not rotaion of {string2}")
main()       
#  Output:
# Enter a string : hello
# Enter a string : olleh
# hello is rotation of olleh
