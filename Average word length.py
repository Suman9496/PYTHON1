def average_word_length(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words) if words else 0
