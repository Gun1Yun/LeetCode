"""
344. Reverse String (https://leetcode.com/problems/reverse-string)
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        for i in range(mid):
            tmp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = tmp
