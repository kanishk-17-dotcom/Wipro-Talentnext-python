                                    # EXERCISES


# Q.1 Write a program to create a list of 5 integers and display the list items. 
# Access individual elements through index.

li = [1,2,3,4,5]
for i in range(len(li)):
    print(li[i],end=" ")


# Q.2 Write a program to append a new item to the end of the list.

li=[1,2,3,4,5,6]
a = int(input("Enter a number to be appended:"))
li.append(a)	
print(li)


# Q.3  Write a program to reverse the order of the items in the list.

li = [1,2,3,4,5,6,7]
print("List Before Reversing:")
print(li)
li.reverse()
print("Reversed list:")
print(li)


# Q.4 Write a program to print the number of occurrences of a specified element in a list. 

li = [1,2,3,4,2,3,5,1,1,6,3,6,1]
print("Occurance of 1 in given list:")
print(li.count(1))


# Q.5 Write a program to append the items of list1 to list2 in the front.

list1 = [1,5,7,9]
list2 = [2,4,6,8]
list2 = list1 + list2
print(list2)


# Q.6 Write a program to insert a new item before the second element in an existing list.

li = [2,4,6,8]
item = 3
li.insert(1,item)
print(li)


# Q.7 Write a program to remove the item from a specified index in a list.

li = [2,4,6,8]
li.pop(1)
print(li)

	
# Q.8 Write a program to remove the first occurrence of a specified element from a list.

li = [2,1,4,1,3,6,1,8]
li.remove(1)
print(li)
