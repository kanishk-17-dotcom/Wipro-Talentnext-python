                              # EXERCISES

# Q.1 Write a program to add a key and value to a dictionary.   
#     Sample Dictionary : {0: 10, 1: 20}
#     Expected Result : {0: 10, 1: 20, 2: 30} 

dic = {"A":10, "B":20}
dic["C"] = 30
print(dic)


# Q.2 Write a program to concatenate the following dictionaries to create a new one.  
#     Sample Dictionary : 
#     dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60} 
#     Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60}
ans = {}
ans.update(dic1) 
ans.update(dic2)
ans.update(dic3)
print(ans)


# Q.3 Write a program to check if a given key already exists in a dictionary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = 4
if key in dic.keys():
    print('True')
else:
    print('False')

# Q.4 Write a program to iterate over a dictionary using for loop and print the keys alone, 
# values alone and both keys and values.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Prtinting only keys:")
for key in dic.keys():
    print(key, end=" ")
print()
print("Printing only values:")
for val in dic.values():
    print(val,end=" ")
print()
print("Printing key and values together:")
for key,val  in dic.items():
    print((key,val),end = " ")


# Q.5 Write a program to prepare a dictionary where the keys are numbers between 1 and 15 
# (both included) and the values are square of the keys.

ans={}
for i in range(1,16):
    ans[i] = i*i
print(ans)


# Q.6 Write a program to sum all the values in a dictionary, considering the values will be of int type.

ans = 0
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for i in dic.keys():
    ans += dic[i]
print("Sum of all values in dictionary is ",ans)