""" 
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def proper_divisor(n):
    divisors = [1]
    i = 2
    while i < n:
        if n%i == 0:
            if i not in divisors:
                divisors.append(int(i))
            else:
                break
            if n/i not in divisors:
                divisors.append(int(n/i))
            else:
                break
        i += 1
    return divisors


def check_abundancy(n):
    '''
    :param n: number to be checked
    :return: 0 if it is deficient; 1 if it is abundant
    '''
    if sum(proper_divisor(n)) < n:
        return 0
    elif sum(proper_divisor(n)) > n:
        return 1


def get_abundant(upper_limit):
    n = 11
    result = []
    while n <= upper_limit:
        n += 1
        if check_abundancy(n):
            result.append(n)
    print(f'There are {len(result)} abundant numbers under {upper_limit}.')
    return result


def get_2sum(num_list):
    res = []
    for i, num in enumerate(num_list):
        j = i
        sum2 = num_list[j] + num
        while sum2 < upper_limit:
            if sum2 not in res:
                res.append(sum2)
            j += 1
            sum2 = num_list[j] + num

    print(f'There are {len(res)} numbers under {upper_limit} can be written as the sum of two abundant numbers.')
    return res


if __name__ == '__main__':
    upper_limit = 1000
    num_list = get_abundant(upper_limit)
    total = 0
    nums_2sum = get_2sum(num_list)
    #
    # print(num_list)
    # print(nums_2sum)

    # for i in range(1, upper_limit+1):
    #     if i not in nums_2sum:
    #         total += i

    for i in range(1, upper_limit + 1):
        total += i
    print(total - sum(nums_2sum))

