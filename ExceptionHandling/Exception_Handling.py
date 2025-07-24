                                   # EXERCISES

# Q.1 Write a program to accept two numbers from the user and perform division. If any exception occurs, 
#     print an error message or else print the result.

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")


# Q.2 Write a program to accept a number from the user and check whether it’s prime or not. If user 
#     enters anything other than number, handle the exception and print an error message.

try:
    n = int(input("Enter a number to check if it's prime: "))
    if n < 2:
        print(f"{n} is not a prime number.")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
except ValueError:
    print("Please enter a valid integer.")


# Q.3 Write a program to accept the file name to be opened from the user, if file exist print the 
#     contents of the file in title case or else handle the exception and print an error message.
	
try:
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents.title())
except FileNotFoundError:
    print("Error: File does not exist.")
except Exception as e:
    print("Error:", e)


# Q.4 Declare a list with 10 integers and ask the user to enter an index. Check whether the number in 
#     that index is positive or negative number. If any invalid index is entered, handle the 
#     exception and print an error message.

numbers = [5, -3, 7, -1, 9, -6, 2, 0, -8, 4]
try:
    index = int(input("Enter an index (0-9): "))
    num = numbers[index]
    if num > 0:
        print(f"The number at index {index} is positive.")
    elif num < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")
except IndexError:
    print("Error: Index out of range. Please enter between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")