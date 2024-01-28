/*
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
*/

function groupAnagrams(strs: string[]): string[][] {
    const sortedWordDict: Map<string, string[]> = new Map();
    for (let i = 0; i < strs.length; i++) {
        const sorted = Array.from(strs[i]).sort().join("");
        if (!sortedWordDict.has(sorted)) {
            sortedWordDict.set(sorted, [strs[i]]);
        } else {
            sortedWordDict.get(sorted)?.push(strs[i]);
        }
    }
    const res: string[][] = [];
    sortedWordDict.forEach((word) => {
        res.push(word);
    });
    return res;
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
console.log(groupAnagrams([""]));
console.log(groupAnagrams(["a"]));
