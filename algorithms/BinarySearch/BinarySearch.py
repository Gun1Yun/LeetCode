"""
704. Binary Search (https://leetcode.com/problems/binary-search)

* You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def search(nums: List[int], target: int) -> int:

    start = 0
    end = len(nums) - 1

    while True:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

        if end < start:
            return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))
