class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        i = 0

        while i < m:
            if flowerbed[i] == 1:
                i += 1
            elif i + 1 < m and flowerbed[i + 1] == 1:
                i += 2
            else: 
                i += 1
                n -= 1
            i += 1
        return n <= 0