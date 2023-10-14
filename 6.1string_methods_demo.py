message = " Hello World "
# 1 - Remove the white spaces in start and end 
# of the string "message" 
answer = message.strip()
print(answer)

website = "https://www.github.com/boraswim/Python_tutorials"
# 2 - Remove everything in the string "website" 
# except "Python_tutorial"
answer = website.strip('htps:/www.giubcomras') # Remove given characters
print(answer)

description = "A set of Python essential tutorials I gathered together throughout my learning process."
# 3 - Turn the string "description" to lowercase
answer = description.lower()
print(answer)

website = "https://www.github.com/boraswim/Python_tutorials" # Reassign
# 4 - Find the amount of letter 'a' in the string "website"
answer = website.count('a')
print(answer)

# 5 - Check if the string "website" starts with "www" or not
answer = website.startswith("www")
print(answer)

# 6 - Check if the string "website" contains ".com" or not
answer = website.find(".com")
print(".com was found at the index", answer)

# 7 - Check if all the letters in "website" are alphabetic
answer = description.isalpha() # Check if all letters are alpha (a-z)
print(answer)

message = "Table of Contents"
# 8 - Center the string "Table of Contents" in 50 spaces
# and add '*' to left and right
answer = message.center(50, '*')
print(answer)

# Replace all the whitespace with '-'
# in the string "description"
answer = description.replace(' ', '-')
print(answer)

message = "Hello world" # Reassign
# Replace "world" with "galaxy"
# in the string "message"
answer = message.replace("world", "galaxy")
print(answer)

# Seperate words of the string "description"
# from whitespaces and store them in an array 
answer = description.split(' ')
print(answer)