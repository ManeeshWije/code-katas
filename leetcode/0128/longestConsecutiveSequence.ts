// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
//
// You must write an algorithm that runs in O(n) time.
//
//
//
// Example 1:
//
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
// Example 2:
//
// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9
//
//
// Constraints:
//
// 0 <= nums.length <= 105
// -109 <= nums[i] <= 109

function longestConsecutiveSequence(nums: number[]): number {
    // if (nums.length === 0) return 0;
    // if (nums.length === 1) return 1;
    // // sorted way
    // const sorted = Array.from(nums).sort((a, b) => a - b);
    // const possible: number[] = [];
    // console.log(sorted);
    // let res = 1;
    // for (let i = 0; i < sorted.length - 1; i++) {
    //     if (sorted[i] === sorted[i + 1]) continue;
    //     if (sorted[i] + 1 === sorted[i + 1]) {
    //         res++;
    //     } else {
    //         res = 1;
    //     }
    //     possible.push(res);
    // }
    // console.log(possible);
    // let final = 1;
    // for (let i = 0; i < possible.length; i++) {
    //     final = Math.max(final, possible[i]);
    // }
    // return final;

    // non sorted way
    if (nums.length === 0) return 0;
    if (nums.length === 1) return 1;
    const setNum = new Set(nums);
    let res = 0;
    for (let i = 0; i < nums.length; i++) {
        if (!setNum.has(nums[i] - 1)) {
            let length = 0
            while (setNum.has(nums[i] + length)) {
                length++
            }
            res = Math.max(res, length)
        }
    }
    return res
}

console.log(longestConsecutiveSequence([100, 4, 200, 1, 3, 2]));
console.log(longestConsecutiveSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));
console.log(longestConsecutiveSequence([1, 2, 0, 1]));
console.log(longestConsecutiveSequence([0, 0]));
