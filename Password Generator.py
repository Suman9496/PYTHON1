import random


def generate_password(length=12, complexity="medium"):
    password = ""

    if complexity == "low":
        chars = "abcdefghijklmnopqrstuvwxyz"
    elif complexity == "medium":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif complexity == "high":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    for _ in range(length):
        password += random.choice(chars)

    return password


print(generate_password(16, "high"))
