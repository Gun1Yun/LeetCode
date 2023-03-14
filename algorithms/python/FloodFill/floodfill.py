"""
733. Flood Fill (https://leetcode.com/problems/flood-fill/)
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
        center = [(sr, sc)]
        
        while center:
            r, c = center.pop()
            image[r][c] = color
            directions = []
            if r-1 >= 0:
                directions.append((r-1, c)) # up
            if r+1 < len(image):
                directions.append((r+1, c)) # down
            if c-1 >= 0:
                directions.append((r, c-1)) # left
            if c+1 < len(image[0]):
                directions.append((r, c+1)) # right

            for d in directions:
                n_r, n_c = d
                if image[n_r][n_c]==start_color:
                    center.append((n_r, n_c))

        return image
                
            