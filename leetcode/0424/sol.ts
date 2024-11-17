/*
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

 

Constraints:

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length
*/

function characterReplacement(s: string, k: number): number {
    let left = 0;
    let right = 0;
    let res = 0;
    let freq: Map<string, number> = new Map();

    while (right < s.length) {
        if (freq.get(s[right])) {
            freq.set(s[right], freq.get(s[right])! + 1);
        } else {
            freq.set(s[right], 1);
        }
        let windowSize = right - left + 1;
        if (windowSize - Math.max(...freq.values()) <= k) {
            res = Math.max(res, windowSize);
        } else {
            freq.set(s[left], freq.get(s[left])! - 1);
            left++;
        }
        right++;
    }
    return res;
}

console.log(characterReplacement("ABAB", 2));
console.log(characterReplacement("AABABBA", 1));
