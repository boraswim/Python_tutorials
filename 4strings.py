name = "Bora"       # Strings are arrays of chars
surname = "Sevim"
age = 36

# Using + operator with strings to concatenate them (\n = new line)
print("My name is " + name + " " + surname + " and\nI am " + str(age) + " years old.")

greeting = "My name is " + name + " " + surname + " and\nI am " + str(age) + " years old."
print(greeting)

# Print first character of the string "greeting" 
# by starting from index 0
print(greeting[0])

# Print fourth character of the string "greeting"
# (0,1,2,3...)
print(greeting[3])

# Print character length of the string "greeting"
print(len(greeting))

# Print last character of the string "greeting"
# substract 1 from length since index start from 0
length = len(greeting)
print(greeting[length-1])

# Same with "greeting[length-1]"
print(greeting[-1])

# Print the string "greeting" from index 3 to 6
print(greeting[3:6])

# Print the string "greeting" starting from index 3
print(greeting[3:])

# Print the string "greeting" ending with index 15
print(greeting[:15])

# Print the string "greeting" from index 2 to 40
# with increment of 2 (1 is the default value)
print(greeting[2:40:2])