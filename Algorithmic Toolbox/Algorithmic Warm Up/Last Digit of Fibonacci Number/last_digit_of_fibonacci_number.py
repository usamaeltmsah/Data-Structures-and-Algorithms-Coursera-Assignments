# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


# Fast doubling Fibonacci
# fib(n) Returns the tuple (F(n), F(n+1)).
def fib(n):
    if n == 0:
        return 0, 1
    prev, curr = fib(n // 2)
    c = prev * (curr * 2 - prev)
    d = prev ** 2 + curr ** 2
    if n % 2 == 0:
        return c, d
    return d, c + d


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    return fib(n)[0] % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
