import re

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    result = False
    if len(s) == 0:
        result = True
    pattern = re.compile('[\W_]+')
    s= pattern.sub('', s).lower()
    if s[::-1] == s:
        result = True
    return result


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
    print(isPalindrome(''))
    print(isPalindrome("a"))