class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        left = height[i]
        right = height[j]
        maxS = min(left, right) * (j - i)
        while i != j:
            if left <= right:
                i += 1
                if left < height[i]:
                    s = min(height[i], right) * (j - i)
                    if maxS <= s:
                        maxS = s
                left = height[i]
            else:
                j -= 1
                if right < height[j]:
                    s = min(height[j], left) * (j - i)
                    if maxS <= s:
                        maxS = s
                right = height[j]
        return maxS