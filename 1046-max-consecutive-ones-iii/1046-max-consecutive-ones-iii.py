class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        best = 0

        for r in range(len(nums)):
            if not nums[r]:
                zeros += 1
            
            while zeros > k:
                if not nums[l]:
                    zeros -= 1
                l += 1
                
            best = max(best, r-l+1)
        
        return best