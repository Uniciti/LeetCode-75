class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for v in nums:
            if v <= first:
                first = v
            elif v <= second:
                second = v
            else:
                return True
            
        return False