class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}
        for i in word1:
            d1[i] = d1.get(i, 0) + 1
        for i in word2:
            d2[i] = d2.get(i, 0) + 1

        return (sorted(d1.values()) == sorted(d2.values())) and (sorted(d1.keys()) == sorted(d2.keys())) 