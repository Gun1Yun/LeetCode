"""
1. Two Sum (https://leetcode.com/problems/two-sum)

* Can you come up with an algorithm that is less than O(n2) time complexity?.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_indices = sorted(range(len(nums)),key=nums.__getitem__)
        left=0
        right = len(nums)-1
        while True:
            two_sum = nums[sorted_indices[left]]+nums[sorted_indices[right]]
            if two_sum==target:
                return [sorted_indices[left], sorted_indices[right]]
            elif two_sum<target:
                left+=1
            else:
                right-=1