"""
567. Permutation in String (https://leetcode.com/problems/permutation-in-string)

*  1 <= s1.length, s2.length <= 104
"""
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        idx = 0
        window_size = len(s1)
        s1_counter = Counter(s1)

        while idx+window_size <= len(s2):
            sub = s2[idx:idx+window_size]
            sub_counter = Counter(sub)

            if s1_counter == sub_counter:
                return True
            idx += 1

        return False
            


