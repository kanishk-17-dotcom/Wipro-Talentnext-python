                                     # EXERCISES 

# Q.1 Write a LC program to create an output dictionary which contains only the odd numbers that are 
    # present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values.

list_1 = [1,2,3,4,5,6,7]
dic = {n:n**3 for n in list_1 if n%2==1}
print(dic)


# Q.2 Make a dictionary of the 26 english alphabets mapping each with the corresponding integer.

lis = {chr(ord('a')+i):i+1 for i in range(26)}
print(lis)