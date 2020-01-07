""" 
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""


def sum_amicable(n):
    total = 0
    for i in range(n+1):
        a = i
        b = sum(proper_divisor(i))
        if sum(proper_divisor(b)) == a:
            total += a
    return total


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


if __name__ == '__main__':
    n = 100
    print(sum_amicable(n))
