import math

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        result = 0
        for x in nums:
            count[x] = count.get(x, 0) + 1
        for x in count.keys():
            y = k - x
            if y == x:
                result += math.floor(count.get(x) / 2)
                count[x] = count.get(x, 0) % 2

            else:
                min_key = x if count.get(x,0) < count.get(y,0) else y
                result += min(count.get(x), count.get(y, 0))
                if min_key in count:
                    count[min_key] = 0
        return result