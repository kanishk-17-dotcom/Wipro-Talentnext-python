                                    # EXERCISES

# Q.1 Write a function to return the sum of all numbers in a list.  
#     Sample List : (8, 2, 3, 0, 7)
#     Expected Output : 20

def sum_list(li):
    return sum(li)
li = [8,2,3,0,7]
print(sum_list(li))


# Q.2 Write a function to return the reverse of a string.  
#     Sample String : "1234abcd"
#     Expected Output : "dcba4321"

def reverse_string(str):
    return str[::-1]
s = input("Enter the string :")
print(reverse_string(s))


# Q.3 Write a function to calculate and return the factorial of a number (a non-negative integer).

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
number = int(input("Enter a number :"))
print(fact(number))	


# Q.4 Write a function that accepts a string and prints the number of upper case letters and lower 
#     case letters in it. 

def count_u_l(str):
    l = 0
    u = 0
    for i in str:
        if i.islower() :
            l += 1
        elif i.isupper() :
            u += 1
    return l,u
s = input("Enter the string :")
lower , upper = count_u_l(s)
print("Count of lower case :",lower)
print("Count of upper case :",upper)


# Q.5 Write a function to print the even numbers from a given list. List is passed to the function 
#     as an argument. 
#     Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     Expected Result : [2, 4, 6, 8]
	
def even(l):
    ans =[]
    for i in l:
        if i % 2 == 0 :
            ans.append(i)
    return ans 
li = [1,2,3,4,5,6,7,8,9]
print(even(li))


# Q.6 Write a function that takes a number as a parameter and checks whether the number is prime or not.

def prime(n):
    if n < 2 :
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number:"))
if prime(number) :
    print("The number is prime")
else:
    print("The number is composite")