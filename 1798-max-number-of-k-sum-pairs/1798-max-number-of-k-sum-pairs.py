class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c_dict = Counter(nums)
        result = 0

        for x in c_dict:
            y = k - x

            if x == y and y in c_dict:
                result += c_dict[x] // 2
            elif x < y and y in c_dict:
                result += min(c_dict[x], c_dict[y])
                
        return result
