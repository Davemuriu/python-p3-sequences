#!/usr/bin/env python3

def print_fibonacci(length):
    """Print the first `length` Fibonacci numbers as a list."""
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    print(fib_sequence)


# Example usage
if __name__ == "__main__":
    print_fibonacci(9)
    # => [0, 1, 1, 2, 3, 5, 8, 13, 21]
