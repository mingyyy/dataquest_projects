""" 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# c max: 997 while a = 1 and b = 2 both min
# c min: 335 while a = 332 and b = 333 both max


for c in range(335, 998):
    b = c - 2
    counter = 1
    while 2 < b < c:
        counter += 1
        b = c - counter
        a = 1000 - b - c
        if 0 < a < b:
            if a**2 + b**2 == c**2:
                print(a, b, c)

# 200 375 425