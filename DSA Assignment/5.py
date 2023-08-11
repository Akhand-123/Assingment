# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print (f"Move disk 1 from source {source} to destination {destination}")
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print (f"Move disk {n} from source {source} to destination {destination}")
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = int(input("Enter the no. of disk in tower "))
# function calling 
res=TowerOfHanoi(n,'A','B','C')

# output
# Enter the no. of disk in tower 4
# Move disk 1 from source A to destination C
# Move disk 2 from source A to destination B
# Move disk 1 from source C to destination B
# Move disk 3 from source A to destination C
# Move disk 1 from source B to destination A
# Move disk 2 from source B to destination C
# Move disk 1 from source A to destination C
# Move disk 4 from source A to destination B
# Move disk 1 from source C to destination B
# Move disk 2 from source C to destination A
# Move disk 1 from source B to destination A
# Move disk 3 from source C to destination B
# Move disk 1 from source A to destination C
# Move disk 2 from source A to destination B
# Move disk 1 from source C to destination B
