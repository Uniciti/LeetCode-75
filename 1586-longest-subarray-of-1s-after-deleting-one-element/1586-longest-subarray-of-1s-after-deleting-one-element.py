class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        best = 0
        zeros = 0
        l = 0

        for r in range(len(nums)):
            if not nums[r]:
                zeros += 1

            while zeros > 1: 
                if not nums[l]:
                    zeros -= 1
                l += 1
            
            best = max(best, r-l)

        return best