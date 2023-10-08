"""
Used for comment blocks
"""

"""
1 - Create the variables needed for customer name, surname,
    full name, sex, id, birthyear, address, age
"""
customerName = "John"
customerSurname = "Doe"
customerFullName = customerName + " " + customerSurname
print(customerFullName) # John Doe
customerSex = True # True for male, false for female
customerId = 4096
customerBirthYear = 2000
customerAddress = "Paris/France"
customerAge = 2023 - customerBirthYear

""" 
2 - Find the sum of orders
    Order 1 => 110      $
    Order 2 => 1100.5   $
    Order 3 => 356.95   $
"""
order1, order2, order3 = (110, 1100.5, 356.95)
sum = order1 + order2 + order3
print("Total: ", total) # Total: 1567.45