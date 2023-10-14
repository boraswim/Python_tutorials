"""
Area of circle formula: πr²
Perimeter of circle formula: 2πr

1 - Calculate perimeter and area of the circle with given radius 
    (π=3.14)
"""

pi = 3.14   # Constant

# Get value of radius from user then convert to float
radius = float(input("Radius of circle:")) 

# Calculate perimeter and area of circle
perimeter = 2*pi*radius
area = pi * (radius ** 2)

# Print the calculated values
print("Circle perimeter: ",perimeter,"\nCirlce area: ",area)




