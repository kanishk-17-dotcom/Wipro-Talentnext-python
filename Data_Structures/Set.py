                             # EXERCISES

# Q.1 Write a program to remove a given item from the set.

s = {"Hello","Hi","Hola","World"}
s.remove("World")
print(s)

	
# Q.2 Write a program to create an intersection of sets.

s1 = {1,2,3,4,5,6,7,8,9}
s2 = {2,4,6,8,10,12}
s = s1 & s2
print(s)


# Q.3 Write a program to create an union of sets.

s1 = {1,2,3,4,5,6,7,8,9}
s2 = {2,4,6,8,10,12}
s = s1 | s2
print(s)
	

# Q.4 Write a program to find the maximum and minimum value in a set.

s1 = {1,2,3,4,5,6,7,8,9}
maxs = max(s1)
mins = min(s1)
print("Maximum value in set :",maxs)
print("Minimum value in set :",mins)