def square_sum(numbers):
    sum_of_squares = 0
    for number in numbers:
        square = number * number
        sum_of_squares += square
    return sum_of_squares
