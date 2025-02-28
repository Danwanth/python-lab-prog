import math

print("Enter the coefficients for the quadratic equation")
print("ax^2 + bx + c = 0")

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"The roots of the equation are real and different: {root1} and {root2}")
elif d == 0:
    root = -b / (2 * a)
    print(f"The roots of the equation are real and the same: {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-d) / (2 * a)
    print(f"The roots of the equation are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
