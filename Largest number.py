def find_largest_number(numbers):


  largest_number = numbers[0]
  for number in numbers:
    if number > largest_number:
      largest_number = number
  return largest_number


# Example usage:

numbers = [1, 5, 3, 7, 2]
largest_number = find_largest_number(numbers)

print(largest_number)
