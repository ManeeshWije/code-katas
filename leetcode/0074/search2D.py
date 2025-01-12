"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # first find potential row
    l = 0
    r = len(matrix) - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[m][-1]:
            l = m + 1
        elif target < matrix[m][0]:
            r = m - 1
        else:
            break

    m = (l + r) // 2
    ll = 0
    rr = len(matrix[0]) - 1
    while ll <= rr:
        mm = (ll + rr) // 2
        if target > matrix[m][mm]:
            ll = mm + 1
        elif target < matrix[m][mm]:
            rr = mm - 1
        else:
            return True

    return False




print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(searchMatrix([[1]], 1))
