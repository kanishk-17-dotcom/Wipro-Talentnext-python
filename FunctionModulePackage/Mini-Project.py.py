"""
1.
Write a Python function that accepts a hyphen - separated sequence of colors as input and returns the 
colors in a hyphen - separated sequence after sorting them alphabetically.

Constraint : All the colors will be completely in either lower case or upper case.

Sample input 1: green-red-yellow-black-white

Sample output 1: black-green-red-white-yellow

Sample input 2: PINK-BLUE-TAN-PURPLE

Sample output 2: BLUE-PINK-PURPLE-TAN
"""

def sort_colors(colors: str):
    color_list = colors.split('-')
    color_list.sort()
    return '-'.join(color_list)
colors = input('Enter hyphen seperated colors: ')
print('Sorted List:',sort_colors(colors))



"""
2.
Create a Python module with the following functions:
Function Name              :                Task
ispalindrome(name): Given the user name as input, this function should tell us whether the name is a 
                    palindrome or not.
count_the_vowels (name): Given the user name as input, this function should tell us how many vowels 
                         are present in it.
frequency_of_letters(name): Given the user name as input, this function should tell us how many times 
                            each letter appears in the name.

Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing appropriate inputs.

Sample input 1: bob

Sample output 1:

Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, 0-1

Sample input 2: marcel bentok tanaka

Sample output 2:

No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, г-1, c-1, e-2, 1-1, b-1, n-2, t-2, 0-1, k-2

"""

# The module is named as string_functions inside the same folder
import string_func
string = input("Enter name: ")
string_func.ispalindrome(string)
string_func.count_the_vowels(string)
string_func.frequency_of_letters(string)