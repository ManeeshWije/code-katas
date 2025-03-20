"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

Example 1:
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation:
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

Constraints:
nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
"""

from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        for k, v in freq.items():
            if v % 2 != 0:
                return False
        return True
        # O(n) time and O(n) space
        # For less space we can use a set where we add the element and then delete it when seen again
        # If at the end we still have elements in the set, then it is not possible


sol = Solution()
print(sol.divideArray([3, 2, 3, 2, 2, 2]))
print(sol.divideArray([1, 2, 3, 4]))
