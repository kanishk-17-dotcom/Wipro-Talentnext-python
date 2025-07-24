                                   # EXERCISES

# Q.1 Write a program to count the number of upper and lower case letters in a String.

str = "HellO WorlD"
lower = 0
upper = 0
for i in str:
    if i.islower() :
        lower += 1
    elif i.isupper() :
        upper += 1
    else:
        pass
print("Count of lower case is: ", lower)
print("Count of upper case is: ",upper)


# Q.2 Write a program that will check whether a given String is Palindrome or not.

str = input("Enter a string:")
new_str = str[::-1]
if str == new_str :
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")


# Q.3 Given a string, return a new string made of n copies of the first 2 chars of the original string
#     where n is the length of the string. The string length will be >=2. 
#     If input is "Wipro" then output should be "WiWiWiWiWi".

str = input("Enter a string: ")
n = len(str)
substr = str[:2]
print(substr*n)

# Q.4 Given a string, if the first or last character is 'x', return the string without those 'x' character, 
#     else return the string unchanged. If the input is "xHix", then output is "Hi".

str = input("Enter a string: ")
if str[0] == "x" and str[-1] == "x" :
    print(str[1:len(str)-1])
else:
    print(str)


# Q.5 Given a string and an integer n, return a string made of n repetitions of the last n characters 
#     of the string. You may assume that n is between 0 and the length of the string inclusive.
#     For example if the inputs are "Wipro" and 3, then the output should be "propropro".

str = input("Enter a string: ")
n = int(input("Enter a number :"))
ans = n*(str[-n:])
print(ans)