class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        n = len(nums)
        while j < n and i < n:
            if nums[i] != 0:
                i += 1
            elif nums[j] == 0:
                j += 1
            elif i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                j += 1