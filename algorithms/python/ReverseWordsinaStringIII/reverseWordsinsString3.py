"""
557. Reverse Words in a String III (https://leetcode.com/problems/reverse-words-in-a-string-iii)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(list(map(lambda x: x[::-1], s)))
