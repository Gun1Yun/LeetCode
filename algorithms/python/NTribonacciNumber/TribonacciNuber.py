"""
1137. N-th Tribonacci Number (https://leetcode.com/problems/n-th-tribonacci-number/)
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        def tribo(k, answer):
            if k <= 2:
                return answer[k]
            if answer[k]==0:
                answer[k] = tribo(k-1, answer) + tribo(k-2, answer) + tribo(k-3, answer)
            return answer[k]
            
        answer = [0, 1, 1]
        answer += [0]*(n-2)

        return tribo(n, answer)