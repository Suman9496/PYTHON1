import random


def generate_poem():
    poem = ""

    # Generate a random number of stanzas
    stanzas = random.randint(2, 5)

    for i in range(stanzas):
        # Generate a random number of lines for each stanza
        lines = random.randint(3, 5)

        for j in range(lines):
            # Generate a random line of poetry
            poem += random.choice([
                "Roses are red, violets are blue",
                "I love to code, it's so much fun",
                "Python is the best programming language",
                "I'm Bard, the AI language model",
                "I'm here to help you with your Python needs"
            ])

        poem += "\n"

    return poem


print(generate_poem())
