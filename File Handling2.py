# Open a file for reading
file = open("my_file.txt", "r")

# Read the contents of the file
contents = file.read()

# Close the file
file.close()

# Write to a file
file = open("my_file.txt", "w")

file.write("This is some new text.")

file.close()
