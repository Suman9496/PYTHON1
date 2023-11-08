nouns = ["apple", "banana", "orange"]
verbs = ["eat", "drink", "play"]
adjectives = ["red", "yellow", "green"]

def generate_mad_libs():
    mad_lib = ""
    mad_lib += "I went to the store to buy a "
    mad_lib += random.choice(nouns) + "."
    mad_lib += " I decided to "
    mad_lib += random.choice(verbs) + " it."
    mad_lib += " It tasted very "
    mad_lib += random.choice(adjectives) + "."

    return mad_lib

print(generate_mad_libs())
