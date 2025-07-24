                            # EXERCISES

# Q1. Write a program to check if a given number is Positive, Negative or Zero.

num = int(input("Enter the number:"))
if num == 0:
    print("The number entered is zero.")
elif num > 0 :
    print("The number entered is positive.")
else:
    print("The number entered is negative.")
    

# Q2. Write a program to check if a given number is odd or even.

num = int(input("Enter the number:"))
if num % 2 == 0 :
    print("The number entered is even.")
else:
    print("The number entered is odd.")


# Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
x = a%10
y = b%10
if x==y:
    print("True")
else:
    print("False")


# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

for i in range(11) :       
    print(i,end=" ")


# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

for i in range(23,58) :
    if i % 2 == 0 :
        print(i)


# Q6. Write a program to check if a given number is prime or not.

num = int(input("Enter the number:"))
if num <= 1 :
    print("The number is not prime.")
else:
    for i in range(2,int(num*0.5)+1) :
        if num % i == 0 :
            print("The number is not prime(is composite).")
            break
    else:
        print((("The number is prime number.")))

        
# Q7. Write a program to print prime numbers between 10 and 99.

for num in range(10,100) :
    for i in range(2,int(num*0.5)+1) :
        if num % i == 0 :
            break
    else:
        print(num)


# Q8. Write a program to print the sum of all the digits of a given number.

num = int(input("Enter the number:"))
sum = 0
while num :
    digit = num % 10 
    sum += digit
    num = num // 10
print(f"The sum of digits of given number is {sum}")


# Q9. Write a program to reverse a given number and print.

num = int(input("Enter the number:"))
newnum = 0
while num :
    digit = num % 10
    newnum = newnum*10 + digit 
    num = num // 10
print(f"The reverse of gien number is {newnum}")


# Q10. Write a program to find if the given number is palindrome or not.

num = int(input("Enter the number:"))
temp = num
newnum = 0
while temp :
    digit = temp % 10
    newnum = newnum*10 + digit 
    temp = temp // 10
if num == newnum :
    print("The number is palindrome.")
else:
    print("The number is not a palindrome.")


