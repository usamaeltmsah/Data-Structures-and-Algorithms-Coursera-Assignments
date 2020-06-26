# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    maxi1 = max(numbers)
    numbers.remove(maxi1)
    maxi2 = max(numbers)

    return maxi1 * maxi2

# def max_pairwise_product(numbers):
#     assert len(numbers) >= 2
#     assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
#     maxi1 = -math.inf
#     max_ind1 = 0
#     maxi2 = -math.inf
#     l = len(numbers)
#     for i in range(l):
#         if numbers[i] > maxi1:
#             max_ind1 = i
#             maxi1 = numbers[i]
#     for i in range(l):
#         if i != max_ind1 and numbers[i] > maxi2:
#             maxi2 = numbers[i]
#
#     return maxi1 * maxi2


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
