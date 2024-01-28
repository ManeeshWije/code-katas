/*
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
*/

function validAnagram(s: string, t: string): boolean {
    // return Array.from(s).sort().join("") === Array.from(t).sort().join("")
    const sMap: Map<string, number> = new Map();
    const tMap: Map<string, number> = new Map();
    for (let i = 0; i < s.length; i++) {
        if (!sMap.has(s[i])) {
            sMap.set(s[i], 1);
        } else {
            let exist = sMap.get(s[i]);
            if (exist) {
                sMap.set(s[i], (exist += 1));
            }
        }
        if (!tMap.has(t[i])) {
            tMap.set(t[i], 1);
        } else {
            let exist = tMap.get(t[i]);
            if (exist) {
                tMap.set(t[i], (exist += 1));
            }
        }
    }

    if (sMap.size !== tMap.size) {
        return false;
    }

    for (const [k, v] of sMap) {
        if (!tMap.has(k)) {
            return false;
        }
        if (tMap.get(k) !== v) {
            return false;
        }
    }
    return true;
}

console.log(validAnagram("anagram", "nagaram"));
console.log(validAnagram("rat", "car"));
