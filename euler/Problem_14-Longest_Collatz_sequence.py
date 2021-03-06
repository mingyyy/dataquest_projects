""" 
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def terms(n):
    counter = 1
    while n != 1:
        if n%2 == 0:
            n = n/2
            counter += 1
        else:
            n = 3*n + 1
            counter += 1
    return counter


longest_chain = 179
number = 871
for n in range(1, 1000000):
    if terms(n) > longest_chain:
        longest_chain = terms(n)
        number = n
print(f'The starting number {number} produces the longest chain: {longest_chain}.')

#less than 1,000,000, The starting number 837799 produces the longest chain: 525.
