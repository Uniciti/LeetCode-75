class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for v in nums:
            if v != 0:
                nums[write] = v
                write += 1
        
        for i in range(write, len(nums)):
            nums[i] = 0