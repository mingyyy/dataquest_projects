def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    flag = 0
    indicator = 1
    if dividend < 0 and divisor < 0:
        dividend = - dividend
        divisor = -divisor
    elif dividend < 0 and divisor > 0:
        indicator = -1
        dividend = - dividend
    elif dividend > 0 and divisor < 0:
        indicator = -1
        divisor = -divisor
    d = divisor
    counter = 0
    if d > dividend:
        return 0
    if d == 1:
        return dividend
    while flag == 0:
        d += divisor
        counter += 1
        if d > dividend:
            flag = 1
    return counter * indicator

if __name__ == "__main__":
    print(divide(-2**31,1))