""" 
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def find_nth(n):
    total = n
    fac_list = []
    for i in range(9, 0, -1):
        fac_list.append(factorial(i))

    num_list = []
    total_list = []
    for i in fac_list:
        multiplier = 1
        if total_list:
            total = total_list[-1]
        while total > i * multiplier:
            multiplier += 1
        num_list.append(multiplier-1)
        total_list.append(total - (multiplier - 1)*i)
    return fac_list, num_list, total_list


if __name__ == '__main__':
    n = 10 ** 6
    print(find_nth(n))
