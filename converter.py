def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


print("Celsius to Fahrenheit:")
print(celsius_to_fahrenheit(20))

print("Fahrenheit to Celsius:")
print(fahrenheit_to_celsius(68))
