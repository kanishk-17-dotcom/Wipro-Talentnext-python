                              # EXERCISES

# Q.1 Write a program to print the 4th element from first and 4th element from last in a tuple.

t = (10, 20, 40, 40, 50, 60,70, 80, 90)
first4 = t[3]
n = (len(t) - 1) - 4
last4 = t[n]
print("4th Element From The First:",first4)
print("4th Element From The Last:",last4)


# Q.2 Write a program to check whether an element exists in a tuple or not.

t = (10, 20, 40, 50, 60,70, 80, 90)
target = int(input("Enter a number to check:"))
for i in t:
    if i == target:
        print("The Number Entered Exist In Tuple")
        break
else:
    print("The Number Does Not Entered Exist In Tuple")


# Q.3 Write a program to convert a list into a tuple.

li = [1,2,3,4,5,6,7,8,9,10]
t = tuple(li)
print(t)


# Q.4 Write a program to find the index of an item in a tuple.

t = (10, 20, 40, 50, 60,70, 80, 90)
target = int(input("Enter a number to check:"))
for i in range(len(t)):
    if t[i] == target:
        print("The Number Entered Exist In Tuple At Index :",i)
        break


# Q.5 Write a program to replace last value of tuples in a list to 100.  
#     Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
#     Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

li = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for index in range(len(li)):
    l = list(li[index])  
    l[-1] = 100 
    li[index] = tuple(l)
print(li)
