print(" ")
print("Area Calulator")
print("______________")

square_length = float(input("What is the length of the side of a square? "))
a = 2
exponentiation = round((square_length ** a),2)
print(f"The area of the square is {exponentiation}.")

rectangle_side1 = float(input("What is the first length of the rectangle? "))
rectangle_side2 = float(input("What is the second length of the rectangle? "))
multiplication = round((rectangle_side1 * rectangle_side2),2)
print(f"The area of the rectangle is {multiplication}.")

radius = float(input("What is the radius of the circle? "))
pi = 3.14
circle_area = round((pi * (radius ** a)),2)
print(f"The area of the circle is {circle_area}.")

height = float(input("What is the height of 90* triangle? "))
base = float(input("What is the base of the 90* triangle? "))
b = 0.5
triangle = round((base * height * b),2)
print(f"The area of the triangle is {triangle}.")
print("______________")