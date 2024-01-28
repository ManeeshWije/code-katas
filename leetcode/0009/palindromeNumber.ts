/*
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?
*/

function palindromNumber(x: number): boolean {
    const strX = x.toString();
    let left = 0;
    let right = strX.length - 1;
    while (left < right) {
        if (strX[right] !== strX[left]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
    // follow up is some dumb math stuff thats not applicable at all
}

console.log(palindromNumber(121));
console.log(palindromNumber(-121));
console.log(palindromNumber(10));
