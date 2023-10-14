name = "Bora"
surname = "Sevim"
age = 20

# Place the variables name and surname 
# where the curly brackets are; ordered by index
print("My name is {} {}".format(name, surname))

# Changing the order of index
print("My name is {1} {0}".format(name, surname))

# Indicating order by defined letters n and s
print("My name is {s} {n}".format(n = name, s = surname))

# Other data types can be used in formating too
print("My name is {} {} and I am {} years old.".format(name, surname, age))

# Format the result to show 3 decimal places 
# ({r:1.3})
result = 200 / 700
print("The result is {r:1.3}".format(r = result))

# Another way of string formatting
print(f"My name is {name} {surname} and I am {age} years old.")


