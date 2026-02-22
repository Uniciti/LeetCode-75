class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_cand = max(candies)
        for v in candies:
            if v + extraCandies >= max_cand:
                result.append(True)
            else:
                result.append(False)
        return result