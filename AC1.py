# Solve a quadratic equation ax² + bx + c = 0

a = float(input("Enter coefficient 'a': "))
b = float(input("Enter coefficient 'b': "))
c = float(input("Enter coefficient 'c': "))

delta = b**2 - 4*a*c

root_2 = (-b - delta**(1/2)) / (2*a)
root_1 = (-b + delta**(1/2)) / (2*a)

print(root_1)
print(root_2)

# Check if a year is a leap year
year = int(input("Enter a year: "))

leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Is the year a leap year, true or false? ", leap_year)
