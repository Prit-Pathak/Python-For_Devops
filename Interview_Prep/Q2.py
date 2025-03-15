"""
1.Given a rotated sorted array of unique elements, find the minimum element. Assume the array was initially sorted in ascending order and then rotated.
nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0
"""


def min_search(nums):
    n = len(nums)
    l = 0
    h = n - 1
    while l < h:
        mid = (l + h) // 2
        if nums[mid] > nums[h]:
            l = mid + 1
        else:
            h = mid
    return nums[l]


nums = [4, 5, 6, 7, 0, 1, 2]
res = min_search(nums)
print(res)
