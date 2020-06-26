# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0
    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def fibonacci_number(n):
    # The first two Fibonacci numbers
    prev, curr = 0, 1
    # Base case
    if n <= 1:
        return n
    # Pisano Period for n % 10 is 60
    rem = n % 60
    # Remainder
    if rem == 0:
        return 0
    # The loop will range from 2 to two terms after the remainder
    for i in range(2, rem + 3):
        f = (prev + curr) % 60
        prev, curr = curr, f

    s = curr - 1
    return s


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    if from_index == 0:
        return (fibonacci_number(to_index) - fibonacci_number(from_index)) % 10
    return (fibonacci_number(to_index) - fibonacci_number(from_index - 1)) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
