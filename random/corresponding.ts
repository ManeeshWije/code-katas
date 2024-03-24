// You are given a list of N unique positive numbers ranging from 0 to
// (N -1). Write an algorithm to replace the value of each number with its corresponding index value in the list
//
// Input
// The first line of the input consists of an integer size, representing the size of the list (N).
// The next line consists of N space-separated integers, arr|9), ar11... amis-11 representing the given list of numbers.
//
// Output
// Print N space-separated integers representing the list obtained by replacing the values of the numbers with their corresponding index values in the list.
//
// Constraints
// 0 < size ≤ 105
// 0 ≤ arri] ≤ 105
//
// Note
// All the numbers in the list are unique.
// Example
// Input:
// 4
// [3 2 0 1]
// Output:
// [2 3 1 0]

function corresponding(n: number, nums: number[]): number[] {
    let res = Array(n).fill(0)

    nums.forEach((num, i) => {
        res[num] = i;
    });

    return res;
}

console.log(corresponding(4, [3, 2, 0, 1]));
