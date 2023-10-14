message = "Hello. My name is Bora Sevim"

# Turn all string to uppercase
message = message.upper() 
print(message)

#Turn all string to lowercase
message = message.lower()
print(message)

# Turn all first letters to uppercase
message = message.title()
print(message)

# Turn only first letter to uppercase
message = message.capitalize()
print(message)

# Store the words in a string to an array
message = message.split()
print(message)
print(message[2]) # Print third element of the array

# Combine the words in an array to a string
# adding '*' in between
message = '*'.join(message)
print(message)

# Delete white spaces in the start and end of string
message = "  Test 123  " 
message = message.strip()
print(message)

# Find "123" in the string and return its index
# returns *-1 if not found
index = message.find("123")
print(index)

# Check if the string starts with 'T'
isFound = message.startswith('T')
print(isFound)

# Check if the string ends with '3'
isFound = message.endswith('3')
print(isFound)

# Replace "123" with "456" in the string
message = message.replace("123", "456")
print(message)

# Center the string in 100 spaces
message = message.center(100)
print(message)

"""
You can check out more string methods on
https://docs.python.org/3/library/stdtypes.html#string-methods
https://www.w3schools.com/python/python_ref_string.asp
https://www.geeksforgeeks.org/python-string-methods/
"""