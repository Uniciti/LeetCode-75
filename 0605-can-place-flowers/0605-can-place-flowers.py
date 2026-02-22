class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        prev = 0
        m = len(flowerbed)
        for i in range(m):
            cur = flowerbed[i]
            next = flowerbed[i + 1] if i + 1 < m else 0
            if prev == 0 and cur == 0 and next == 0:
                n -= 1
                prev = 1
                if n == 0:
                    return True
            else:
                prev = cur

        return False