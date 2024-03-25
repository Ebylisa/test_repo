# 1. 
x = 5

if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")
# oooo needs some work
# 2. 
x = 5
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")
# Still missing out
# 3. 
x = 2
y = 5
if (x ** 3 >= y):
    print("GOT QUESTION 3!")
else:
    print("This one didn't work")
# GOT QUESTION 3


# 4. 
country = "Madagascar"
if country == "Madagascar":
    print(f"{country} is in Africa")
else:
    print(f"{country} is not in Africa")
# Madagascar is in Africa
# 5. 
going_places = True
if going_places:
    print("You're going places!")
else:
    print("You prefer to stay at home.")
# You're going places!
# 6. 
altitude = "66000"
if altitude.isdigit():
    print(f"The plane flew at {altitude} feet")
else:
    print(f"{altitude} cannot be converted to a number")
# The plane flew at 66,000 feet