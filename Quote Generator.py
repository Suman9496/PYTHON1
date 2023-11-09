import random

quotes = [
    "The best way to predict the future is to create it.",
    "The only way to do great work is to love what you do.",
    "If you can dream it, you can do it.",
    "Don't be afraid to fail. It's not the end of the world, and in many ways, it's the first step toward learning something and getting better at it.",
    "The future belongs to those who believe in the beauty of their dreams."
]

def generate_quote():
    quote = random.choice(quotes)
    return quote

print(generate_quote())
