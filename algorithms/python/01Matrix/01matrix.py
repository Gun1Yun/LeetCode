"""
542. 01 Matrix (https://leetcode.com/problems/01-matrix/)

# Solution1 : BFS solutions
# solution2 : DP solutions
"""
from collections import deque


class Solution1:
    # BFS solutions
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        def check(r, c):
            if 0 <= r < m and 0 <= c < n:
                return True
            return False

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))  # append cell
                else:
                    mat[i][j] = -1  # not visited

        while queue:
            r, c = queue.popleft()
            directions = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            for d in directions:
                new_r, new_c = d
                if check(new_r, new_c) and mat[new_r][new_c] == -1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append((new_r, new_c))

        return mat


# DP
class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        def check(r, c):
            if 0 <= r < m and 0 <= c < n:
                return True
            return False

        # left-upper to right-bottom (top and left)
        for r in range(m):
            for c in range(n):
                # for not zero cell
                if mat[r][c] > 0:
                    # top
                    top = mat[r - 1][c] + 1 if check(r - 1, c) else math.inf
                    left = mat[r][c - 1] + 1 if check(r, c - 1) else math.inf
                    mat[r][c] = min(top, left)

        # Reverse right-bottom to left-upper (bottom and right)
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] + 1 if check(r + 1, c) else math.inf
                    right = mat[r][c + 1] + 1 if check(r, c + 1) else math.inf
                    mat[r][c] = min(mat[r][c], bottom, right)

        return mat
