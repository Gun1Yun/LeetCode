"""
695. Max Area of Island (https://leetcode.com/problems/max-area-of-island/)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_r = len(grid)
        n_c = len(grid[0])
        islands = []

        for r in range(n_r):
            for c in range(n_c):
                if grid[r][c] == 1:
                    islands.append((r, c))

        def check(r, c):
            if 0 <= r < n_r and 0 <= c < n_c:
                if grid[r][c] == 1:
                    return True
            return False

        max_area = 0
        visited = [[0 for c in range(n_c)] for r in range(n_r)]

        for start in islands:
            s_r, s_c = start
            
            if visited[s_r][s_c]:
                continue

            area = 0
            visited[s_r][s_c] = 1
            stack = [(s_r, s_c)]

            while stack:
                r, c = stack.pop()
                area+=1
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for d in directions:
                    new_r, new_c = d
                    if check(new_r, new_c):
                        if not visited[new_r][new_c]:
                            visited[new_r][new_c] = 1
                            stack.append((new_r, new_c))

            max_area = max(max_area, area)

        return max_area
                
