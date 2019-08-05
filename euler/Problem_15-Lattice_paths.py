""" 
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""


def factorial(n):
    x=1
    for i in range(1, n+1):
        x *= i
    return x

n = 20
t = int(factorial(2*n)/factorial(n)/factorial(n))
print(f'There are {t} route there through a {n}x{n} grid.')

# x-x-x-x
# x-x-x-x
# x-x-x-x
# x-x-x-x

# 2 x 2: 6 = 3+2+1 = C(4,2)=3*4/2
# 3 x 3: 20 = (4+3+2+1)+(3+2+1)+(2+1)+1 = c(6, 3)=20
# 20 x 20=C(40, 20)=137846528820
