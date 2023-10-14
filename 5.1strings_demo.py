website = "https://www.github.com/boraswim/Python_tutorials"
description = "A set of Python essential tutorials I gathered together throughout my learning process."
# 1 - How many characters are there in the string "description"?
answer = len(description)
print(answer)

# 2 - Get the substring "www" from the string "website"
answer = website[8:11]
print(answer)

# 3 - Get the substring "com" from the string "website"
answer = website[19:22]
print(answer)

# 4 - Take first and last 15 characters from the string "description"
answer = description[:15]
_answer = description[-15:]
print(f"First 15: {answer}\nLast 15: {_answer}")

# 5 - Reverse and print the string "description"
result = description[::-1] # Reverse the string
print(result)

name, surname, age, job = "Bora", "Sevim", 20, "Student"
# 6 - Print "My name is Bora Sevim, I am a 20 years old student."
# with given variables
result=f"My name is {name} {surname}, I am a {age} years old {job}."
print(result)

message = "Hello world"
# 7 - Change the letter "w" with "W" in the string "message"
result = message[:6] + "W" + message[-4:] # Change letter then reassign
print(result)

message = "abc"
# 8 - Print the string "abc" side by side 3 times
result = message * 3
print(result)


