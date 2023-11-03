import math


def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


if __name__ == "__main__":
    a = float(input("Enter the length of side 'a': "))
    b = float(input("Enter the length of side 'b': "))
    c = float(input("Enter the length of side 'c': "))

    if a + b > c and a + c > b and b + c > a:
        area = calculate_area(a, b, c)
        print(f"The area of the triangle is {area:.2f} square units.")
    else:
        print("These side lengths cannot form a triangle.")
