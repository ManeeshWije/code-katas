"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def validAnagram(s, t):
    # if sorted(s) != sorted(t):
    #     return False
    # else:
    #     return True
    # O(nlogn) time 
    # O(1) space
    
    if len(s) != len(t):
        return False
    dS = {}
    dT = {}
    for i in range(len(s)):
        if s[i] not in dS:
            dS[s[i]] = 1
        else:
            dS[s[i]] += 1
        if t[i] not in dT:
            dT[t[i]] = 1
        else:
            dT[t[i]] += 1
    return dS == dT
    # O(n) time 
    # O(1) space due to only being 26 chars, if unicode then O(k) where k is the number of unicode characters

print(validAnagram("anagram", "nagaram"))
print(validAnagram("car", "rat"))
