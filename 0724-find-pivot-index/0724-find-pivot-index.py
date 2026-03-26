class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        left = 0
        right = 0
        total = [0 for _ in range(n)]

        while i < n:
            left += nums[i]
            right += nums[j]
            total[i] += left
            total[j] -= right
            i += 1
            j -= 1

        for i in range(n):
            if total[i] == 0:
                return i
            
        return -1