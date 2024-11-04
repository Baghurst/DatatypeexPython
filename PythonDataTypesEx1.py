#1

print("Hello user")
monday_temp = float(input("Tell me the temperature of this last Monday: "))
tuesday_temp = float(input("Tell me the temperature of this last Tuesday: "))
wednesday_temp = float(input("Tell me the temperature of this last Wednesday: "))
thursday_temp = float(input("Tell me the temperature of this last Thursday: "))
friday_temp = float(input("Tell me the temperature of this last Friday: "))
saturday_temp = float(input("Tell me the temperature of this last Saturday: "))
sunday_temp = float(input("Tell me the temperature of this last Sunday: "))
avgtemp = (monday_temp + tuesday_temp + wednesday_temp + thursday_temp + friday_temp + saturday_temp + sunday_temp) / 7
print(f"The average temperature of this week is {avgtemp}")

#2

import math
PI=3.14
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))
result = 4 * (x ** 4) + 3 * (y ** 3) + 9 * z + 6 * PI
print(f"The result of the expression is: {result}")

#3

seconds = int(input("Enter the number of seconds: "))
minutes = seconds // 60
remaining_seconds = seconds % 60
print(f"{seconds} seconds is {minutes} minutes and {remaining_seconds} seconds.")

#4

hour = int(input("Enter an hour between 1 and 12: "))
hours_ahead = int(input("Enter how many hours ahead: "))
new_hour = (hour + hours_ahead) % 12
if new_hour == 0:
    new_hour = 12
print(f"In {hours_ahead} hours, it will be {new_hour} o'clock.")

#5

number = input("Enter a 3-digit number: ") 
reversed_number = number[::-1] 
print(f"The number reversed is: {reversed_number}")

#6

month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-30): "))

day_of_year = (month - 1) * 30 + day  # Calculate day of the year
print(f"This is day {day_of_year} of the current year.")


