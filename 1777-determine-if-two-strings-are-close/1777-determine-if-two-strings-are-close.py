class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        size1 = len(word1)
        size2 = len(word2)
        if size1 != size2:
            return False
        
        unique1 = len(set(word1))
        unique2 = len(set(word2))
        if unique1 != unique2:
            return False
        
        if len(set(word1)|set(word2)) > unique1:
            return False

        nums1 = []
        for c in set(word1):
            nums1.append(word1.count(c))
        
        nums2 = []
        for c in set(word2):
            nums2.append(word2.count(c))

        nums1.sort()
        nums2.sort()
 
        idx = 0
        while idx < len(nums1):
            if nums1[idx] != nums2[idx]:
                return False
            idx += 1

        return True