""" 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def isprime(x):
    result = True
    for i in range(2, int(x)):
        if x % i == 0:
            result = False
            return result
    return result

# problem with recursive exit()
# factor_list=[]
# def factorize(n):
#     for x in range(2, int(n)):
#         if isprime(x) and n%x == 0:
#             factor_list.append(x)
#             y = int(n/x)
#             if isprime(y):
#                 factor_list.append(y)
#                 break
#             else:
#                 factorize(y)


def primeFact(i, f):
    if i < f:
        return []
    if i % f == 0:
        return [f] + primeFact(i / f, 2)
    return primeFact(i, f + 1)

# print(primeFact(15, 2))

def find_smallest(n):
    l=[]
    res = 1
    for x in range(2, n+1):
        if isprime(x):
            l.append(x)
        else:
            for j in primeFact(x, 2):
                if j in l:
                    l.remove(j)
            l = l + primeFact(x, 2)

    for x in l:
        res *= x
    return res, l
                
print(find_smallest(20))

#(232792560, [11, 13, 7, 2, 17, 2, 3, 3, 19, 2, 2, 5])