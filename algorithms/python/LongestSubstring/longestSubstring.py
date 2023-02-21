"""
3. Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters)

*  0 <= s.length <= 5 * 104
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1
        window_size = 1
        idx = 0

        if not s:
            return 0

        s += " "
        while idx+window_size < len(s):
            sub = s[idx:idx+window_size]
    
            max_len = max(max_len, len(sub))
            if s[idx+window_size] in sub:
                size = list(sub).index(s[idx+window_size])+1
                idx += size
                window_size -= size

            window_size +=1

        return max_len

