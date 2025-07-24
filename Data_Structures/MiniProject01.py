                               # MINI PROJECTS


""" 
1.
Create a dictionary that contains a list of people and one interesting fact about each of them.Display each
person and his or her interesting fact to the screen. Next, change a fact about one of the people.Also 
add an additional person and corresponding fact. Display the new list of people and facts. Run the program 
multiple times and notice if the order changes.

Sample output:

Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane.

Jeff: is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance. 

"""

dic ={}

n = int(input("Enter the number of people:"))
for i in range(n):
    name = input("Enter your name:")
    fact = input("Enter a fact about yourself:")
    dic[name] = fact

print("THE ORIGINAL DICTIONARY IS :")
for k,v in dic.items():
    print(k,": ",v)

change = input("Enter the name for which you want to change the fact:")
changefact = input("Enter the changed fact:")
dic[change] = changefact

newname = input("Enter a new name:")
newfact = input("Enter a fact about yourself:")
dic[newname] = newfact

print("THE CHANGED DICTIONARY IS :")
for key,val in dic.items():
    print(key,": ",val)



""" 
2.
Given the participant's score sheet for your University Sports Day, you are required to find the 
runner-up score. You have scores. Store them in a list and find the score of the runner-up.

Sample input: [2, 3, 6, 6, 5]

Sample output: 5

Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. 
             Hence, we print 5 as the runner-up score. 

"""

scores = [1,2,6,7,8,3,4,5]
max1 = scores[0]
max2 = -1
for i in range(1,len(scores)):
    if scores[i] > max1 :
        max2 = max1
        max1 = scores[i]
    elif max1 > scores[i] and scores[i] > max2 :
        max2 = scores[i]
print("Score of runner-up is :", max2)



""" 
3.
You have a record of n students. Each record contains the student's name, and their percent marks in Math, 
Physics and Chemistry. The marks can be floating values. You are required to save the record in a 
dictionary data type.Student's name is the key. Marks stored in a list is the value. 
The user enters a student's name. Output the average percentage marks obtained by that student.

Formula: (sum of marks) / (no of subjects)

Sample input: { "Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60] }

Sample output:
Enter a name: Malika
Average percentage mark: 56

Explanation: Marks for Malika are [52, 56, 60] whose average is (52+56+60)/3 => 56

"""

marks = { "Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60] }
name = input("Enter the name for which you want average:")
avg = sum(marks[name]) / 3
print("Average percentage marks: ",avg)



"""
4.
Given a string of n words, help Alex to find out how many times his name appears in the string.

Constraint: 1 <= n <= 200

Sample input: Hi Alex ! Welcome Alex ! Bye Alex.

Sample output: 3

Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.

"""

str = input("Enter the string :")
times = str.count("Alex")
print(times)