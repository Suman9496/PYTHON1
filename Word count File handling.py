def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

file_name = "sample.txt"  # Change to the name of your text file
result = count_words(file_name)
print(f"Word count in {file_name}: {result}")
