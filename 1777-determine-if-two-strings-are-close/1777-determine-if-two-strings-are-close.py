class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}
        for i in word1:
            d1[i] = d1.get(i, 0) + 1
        for i in word2:
            d2[i] = d2.get(i, 0) + 1

        f1 = {}
        f2 = {}

        for j in d1.values():
            f1[j] = f1.get(j, 0) + 1
        for j in d2.values():
            f2[j] = f2.get(j, 0) + 1

        return (f1 == f2) and (d1.keys() == d2.keys())