class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [1] * n
        
        suf = 1
        for i in range(n):
            ans[i] = suf
            suf *= nums[i]

        suf = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suf
            suf *= nums[i]

        return ans