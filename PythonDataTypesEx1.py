#1

print("Hello user")
monday_temp = float(input("Tell me the temperature of this last monday: "))
tuesday_temp = float(input("Tell me the temperature of this last tuesday: "))
wednesday_temp = float(input("Tell me the temperature of this last wednesday: "))
thursday_temp = float(input("Tell me the temperature of this last thursday: "))
friday_temp = float(input("Tell me the temperature of this last friday: "))
saturday_temp = float(input("Tell me the temperature of this last saturday: "))
sunday_temp = float(input("Tell me the temperature of this last sunday: "))
avgtemp = monday_temp + tuesday_temp + wednesday_temp + thursday_temp + friday_temp + saturday_temp + sunday_temp / 7
print(f"The average temperature of this week is {avgtemp}")

#2

PI=3.14
x_ = float(input("Enter the value of x: "))
y_ = float(input("Enter the value of y: "))
z_ = float(input("Enter the value of z: "))
print(4*x_**4 + 3*y_**3 + 9*z_ + 6 * PI)
