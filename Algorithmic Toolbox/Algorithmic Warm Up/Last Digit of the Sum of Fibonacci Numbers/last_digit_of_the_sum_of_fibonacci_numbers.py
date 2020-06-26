# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18
    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    # The first two Fibonacci numbers
    prev, curr = 0, 1
    # Base case
    if n <= 1:
        return n
    # Pisano Period for % 10 is 60
    rem = n % 60
    # Remainder
    if rem == 0:
        return 0
    # The loop will range from 2 to
    # two terms after the remainder
    for i in range(2, rem + 3):
        f = (prev + curr) % 60
        prev, curr = curr = f

    s = curr - 1
    return s % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
