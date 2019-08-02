""" 
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def check_palindrome(n):
    # single digit numbers
    ns = [i for i in str(n)]

    if len(ns) % 2 == 0:
        l = int(len(ns)/2)
    else:
        l = int((len(ns)-1)/2)

    first_half = ns[:l]
    second_half = ns[-l:]

    if first_half[::-1] == second_half:
        return True
    else:
        return False


def largest_palindrome_product(d):
    num_upper = int(10**d-1)
    num_lower = int(10**(d-1))

    print(num_lower, num_upper)

    for i in range(num_upper, num_lower, -1):
        for j in range(num_upper,num_lower, -1):
            if check_palindrome(i*j):
                return i, j, i*j

print(largest_palindrome_product(3))

#(995, 583, 580085)