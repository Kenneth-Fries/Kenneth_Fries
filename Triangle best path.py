#https://leetcode.com/problems/triangle/
"""Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""
"""The following solution uses a bottoms up approach, changing values in the
triangle until the top value is changed, and then returns that value."""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2,-1,-1):
            for j,x in enumerate(triangle[i]):
                triangle[i][j] = min([x+triangle[i+1][j],x+triangle[i+1][j+1]])
        return triangle[0][0]
