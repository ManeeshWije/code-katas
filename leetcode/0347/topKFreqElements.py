"""
Given an integer array nums and an integer p, return the p most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], p = 2
Output: [1,2]

Example 2:
Input: nums = [1], p = 1
Output: [1]

Constraints:
1 <= nums.length <= 105

-104 <= nums[i] <= 104

k is in the range [1, the number of unique elements in the array].

It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""



def topKFreqElements(nums, p):
    # freq = {}
    # res = []
    # for i in range(len(nums)):
    #     if nums[i] not in freq:
    #         freq[nums[i]] = 1
    #     else:
    #         freq[nums[i]] += 1
    # sortedDict = sorted(freq.items(), key=lambda x: x[1])
    # for i in range(k):
    #     res.append(sortedDict.pop()[0])
    # return res
    """
    O(n log n) time 
    O(n) space
    """
    import heapq
    freq = {}
    res = []
    heap = []
    for i in range(len(nums)):
        if nums[i] not in freq:
            freq[nums[i]] = 1
        else:
            freq[nums[i]] += 1
    for k, v in freq.items():
        heap.append((-v, k))
    heapq.heapify(heap)
    for _ in range(p):
        res.append(heapq.heappop(heap)[1])
    return res
    """
    O(p log n) time (slightly better)
    O(n) space
    """

print(topKFreqElements([1, 1, 1, 2, 2, 1, 3, 4, 4, 5, 5, 5, 3], 2))
# print(topKFreqElements([1], 1))
