class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frq = {}

        for i in arr:
            frq[i] = frq.get(i, 0) + 1

        frq_list = list(frq.values())
        return len(frq_list) == len(set(frq_list))