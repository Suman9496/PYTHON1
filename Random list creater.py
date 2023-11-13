import random


def generate_random_words(number_of_words):
    words = []
    with open("/usr/share/dict/words", "r") as f:
        for word in f:
            words.append(word.strip())

    random_words = []
    for i in range(number_of_words):
        random_word = random.choice(words)
        random_words.append(random_word)

    return random_words


print(generate_random_words(10))
