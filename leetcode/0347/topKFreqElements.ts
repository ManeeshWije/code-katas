/*
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
*/

function topKFreqElements(nums: number[], p: number): number[] {
    const res: number[] = [];
    const freqMap: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (!freqMap.has(nums[i])) {
            freqMap.set(nums[i], 1);
        } else {
            let exist = freqMap.get(nums[i]);
            if (exist) {
                freqMap.set(nums[i], (exist += 1));
            }
        }
    }
    // sort by value
    const topSorted = new Map(Array.from(freqMap.entries()).sort((a, b) => a[1] - b[1]));

    let idx = 0
    topSorted.forEach((t) => {
        if (idx !== p) {
            res.push(t);
            idx++
        }
    });
    return res;
    // TODO: Figure out heap way later
}

console.log(topKFreqElements([1, 1, 1, 2, 2, 3], 2));
console.log(topKFreqElements([1], 1));
