x = 1
y = 10
​
# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")
​
# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")
​
# Checks if one value is less than another
if x < y:
    print("x is less than y")
​
# Checks if one value is greater than another
if y > x:
    print("y is greater than x")
​
# Checks if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")
​
# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")
​
# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were true")
​
# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")






x = 1
y = 10
​
# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")
​
# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")
​
# Checks if one value is less than another
if x < y:
    print("x is less than y")
​
# Checks if one value is greater than another
if y > x:
    print("y is greater than x")
​
# Checks if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")
​
# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")
​
# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were true")
​
# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")
Collapse








7:20
Conditional Conundrum
2 files 
conditionals_unsolved.py
1 kB PythonClick to view details


README.md
Markdown (raw)Click to view details


New

Richard Merren  7:35 PM
conditionals_solved.py 
# 1. oooo needs some work
x = 5
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")
​
# 2. Question 2 works!
x = 5
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")
​
# 3. GOT QUESTION 3!
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")
​
# 4. Dan is in group three
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]
​
if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")
​
# 5. Can ride bumper cars
height = 66
age = 16
adult_permission = True
​
if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")




















































