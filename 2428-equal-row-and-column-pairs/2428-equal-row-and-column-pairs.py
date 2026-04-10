from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        n = len(grid)

        ans = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            ans += rows[col]

        return ans