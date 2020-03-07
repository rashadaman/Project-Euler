"""
Sum square difference
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
end = 100


def normal_sum_squared(end):
    return (end * (end + 1) // 2) ** 2


def squared_sum(end):
    return end * (end + 1) * (2 * end + 1) // 6


print(normal_sum_squared(end) - squared_sum(end))
