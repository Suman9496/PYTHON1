def remove_vowels(s):
    return ''.join(char for char in s if char.lower() not in 'aeiou')
