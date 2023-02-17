"""
977. Squares of a Sorted Array (https://leetcode.com/problems/squares-of-a-sorted-array)

* Could you find an O(n) solution using a different approach?
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            l_square = nums[left] ** 2
            r_square = nums[right] ** 2
            if l_square <= r_square:
                result.append(r_square)
                right -= 1
            else:
                result.append(l_square)
                left += 1

        return result[::-1]
