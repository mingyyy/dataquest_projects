""" 
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""


def triangle(n):
    s = 0
    for x in range(1, n+1):
        s += x
    return s


def divisors(n):
    counter = 0
    for x in range(1, n+1):
        if n % x == 0:
            counter += 1
    return counter


i = 2079
x = 0
while x <= 400:
    i += 1
    x = max(x, divisors(triangle(i)))
print(f'{i}th triangle number is {triangle(i)} which has {x} divisors.')

# first over 200 divisor:  2015th triangle number is 2031120 which has 240 divisors.
# first over 300 divisor:  2079th triangle number is 2162160 which has 320 divisors.
# first over 400 divisor: