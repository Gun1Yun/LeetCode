"""
283. Move Zeroes (https://leetcode.com/problems/move-zeroes)
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, non_zero = [], []
        for n in nums:
            if n:
                non_zero.append(n)
            else:
                zero.append(n)
        nums[: len(non_zero)] = non_zero
        nums[len(non_zero) :] = zero
