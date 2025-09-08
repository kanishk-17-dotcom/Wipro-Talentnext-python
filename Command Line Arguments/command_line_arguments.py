                                        # EXERCISES

# Q.1 Write a program to accept two numbers as command line arguments and display their sum.

import sys
if len(sys.argv) != 3:
    print("RETRY")
    sys.exit()
a = int(sys.argv[1])
b = int(sys.argv[2])
c = a + b
print("Sum =", c)

	
# Q.2 Write a program to accept a welcome message through command line arguments and display the file 
#     name along with the welcome message.

import sys

if len(sys.argv) < 2:
    print("Please enter a welcome message as a command-line argument.")
else:
    script_name = sys.argv[0]
    welcome_message = " ".join(sys.argv[1:])
    print(f"File Name: {script_name}")
    print(f"Welcome Message: {welcome_message}")


# Q.3 Write a program to accept 10 numbers through command line arguments and calculate the sum of
#     prime numbers among them.

import sys
if len(sys.argv) != 11:
    print("RETRY")
else:
    li = []
    for i in range(1,11) :
        a = int(sys.argv[i])
        if a <= 1:
            continue
        for j in range(2,int(a**0.5)+1):
            if a % j == 0:
                break
        else:
            li.append(a)
    print("Sum of all entered prime numbers is :",sum(li))