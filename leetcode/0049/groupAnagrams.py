"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

def groupAnagrams(strs):
    sortedAnagramMap = {}
    res = []
    for i in range(len(strs)):
        sortedWord = "".join(sorted(strs[i]))
        if sortedWord not in sortedAnagramMap:
            sortedAnagramMap[sortedWord] = [strs[i]]
        else:
            sortedAnagramMap[sortedWord] += [strs[i]]
    for j in sortedAnagramMap.values():
        res.append(j)
    return res
# O(nklogk) time complexity, where n is the length of strs and k is the maximum length of a string in strs. The outer loop has complexity O(n) as we iterate through each string. Then, we sort each string in O(klogk) time 
# O(nk) space complexity, the total information content stored in sortedAnagramMap

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
