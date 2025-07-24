                                # MINI PROJECTS

""" 
1. Create a python program that asks the user how far they want to travel. If they want to travel less 
than three miles tell them to ride Bicycle. If they want to travel more than three miles, but less than 
three hundred miles, tell them to ride Motor-cycle. If they want to travel three hundred miles or more 
tell them to driver Super-Car.

Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination 

"""

distance = int(input("How far would you like to travel? (in miles) : "))
if distance < 3 :
    print("I suggest a BICYCLE for your ride.")
elif distance >= 3 and  distance < 300 :
    print("I suggest a MOTOR-CYCLE for your ride.")
elif distance >= 300 :
    print("I suggest a SUPER-CAR for your ride.")
else:
    print("Please enter a valid distance.")




"""" 
2. Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that 
charges $0.51 per hour. you will launch your services using one server and want to know how much it will 
cost to operate per day, per week, per month.

Write a python program that displays the answers to the following questions:

How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?

"""

hourly_rate = 0.51

daily_cost = hourly_rate * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30  
total_budget = 918
days_with_budget = total_budget / daily_cost

print(f"Cost to operate one server per day: ${daily_cost:.2f}")
print(f"Cost to operate one server per week: ${weekly_cost:.2f}")
print(f"Cost to operate one server per month: ${monthly_cost:.2f}")
print(f"With $918, you can operate the server for approximately {days_with_budget:.2f} days.")