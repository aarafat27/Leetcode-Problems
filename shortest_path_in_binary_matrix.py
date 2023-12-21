'''
problem link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0, 1)])  # (x, y, distance)
        visited[0][0] = True

        while queue:
            x, y, d = queue.popleft()
            if x == n - 1 and y == n - 1:
                return d

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
            for direction in directions:
                a, b = x + direction[0], y + direction[1]
                if a < 0 or a >= n or b < 0 or b >= n or visited[a][b] or grid[a][b] == 1:
                    continue
                queue.append((a, b, d + 1))
                visited[a][b] = True

        return -1
