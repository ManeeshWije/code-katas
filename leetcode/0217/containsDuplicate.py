"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
def containsDuplicate(nums):
    # d = {}
    # for i in range(len(nums)):
    #     if nums[i] not in d:
    #         d[nums[i]] = 1
    #     else:
    #         return True
    # return False
    # O(n) time
    # O(n) space
    return len(nums) != len(set(nums))
    # O(n) time
    # O(n) space

print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

