""" 
The Fibonacci sequence is defined by the recurrence relation:
Hence the first 12 terms will be:
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fibo(n):
    '''
    :param n: number of fibonacci sequence
    :return: list
    '''
    flist = [0, 1]
    i = 1
    num = 1
    while num < 10 ** (n-1):
        num = flist[-1]+flist[-2]
        flist.append(num)
        i += 1
    return i

if __name__ == '__main__':
    print(fibo(1000))
