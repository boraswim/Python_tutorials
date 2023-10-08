# Take input from user and assign it to variable x
x = input("First number:")
y = input("Second number:")

# String concat of variable x and y by default
sum = x + y
print(sum) 

print(type(x)) # Data type of variable x

# Convert types of variable x and y to int 
# then calculate the sum
sum = int(x) + int(y)
print(sum)

x = 5
y = 2.5
name = "Bora"
isDone = True

"""
int, float, str, bool
print(type(x))
print(type(y))
print(type(name))
print(type(isDone))
"""

# Type conversion

# int to float
x = float(x)
print(x)        # 5.0
print(type(x))  # float

# float to int
y = int(y)
print(y)        # 2
print(type(y))  # int

# bool to str
isDone = str(isDone)
print(isDone)       # True
print(type(isDone)) # str

# Reverting the variable isDone back to bool
# before converting to int
isDone = bool(isDone) 

# bool to int
isDone = int(isDone)
print(isDone)
print(type(isDone))

