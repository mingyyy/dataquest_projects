""" 
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""


def Next_Num(current_pos, current_level, prev_level):
    if current_pos == 0 or current_pos == len(current_level)-1:
        total = current_level[current_pos] + prev_level[current_pos]
    else:
        total = current_level[current_pos] + max(prev_level[current_pos - 1], prev_level[current_pos])
    return total

paths = []
def Max_Path_Sum(triangle):
    '''triangle being a list of a list'''
    current_level = 0
    levels = len(triangle)
    for l in range(levels-1, 0, -1):
        n = len(triangle[l])
        current_level = triangle[l]
        prev_level = triangle[l-1]
        total = 0
        for i in range(n):
            total += current_level[i] + Next_Num(i, prev_level)





    total = 0
    return total


if __name__ == '__main__':
    res = Max_Path_Sum([[3],[7, 4],[2, 4, 6],[8, 5, 9, 3]])
    print(res)