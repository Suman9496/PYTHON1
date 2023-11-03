def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence


if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fibonacci_sequence = generate_fibonacci(n)
    print(f"Fibonacci Sequence (first {n} numbers): {fibonacci_sequence}")
