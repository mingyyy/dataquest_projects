def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i+1:]):
            if n+m == target:
                return [i, j+i+1]


if __name__ == "__main__":
    print(twoSum([3,5,6,1], 11))
    print(twoSum([3,1], 4))