"""
189. Rotate Array (https://leetcode.com/problems/rotate-array)

* Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            r = nums.pop()
            nums.insert(0, r)
