class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        point = 0
        max_point = 0
        for i in gain:
            point += i
            if point >= max_point:
                max_point = point

        return max_point