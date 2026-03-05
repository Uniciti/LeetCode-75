class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first_sum = 0
        if k >= len(nums):
            return sum(nums) / k
        else:
            for i in range(k):
                first_sum += nums[i]
        max_sum = first_sum
        for i in range(len(nums) - k):
            first_sum = first_sum + nums[i + k] - nums[i]
            if first_sum >= max_sum:
                max_sum = first_sum
        return max_sum / k