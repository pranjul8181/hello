import sys
x = int(input("x: "))
y = int(input("y: "))

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)
#result = x / y
try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannnot divide by 0.")
    sys.exit(1)
print(f"{x} / {y} = {result}")
