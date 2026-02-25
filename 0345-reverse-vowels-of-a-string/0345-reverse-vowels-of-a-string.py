class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = set("aeiouAEIOU") 
        str_list = list(s)
        l = 0
        r = len(str_list) - 1

        while l < r:
            while l < r and str_list[l] not in vowels_set:
                l += 1
            while l < r and str_list[r] not in vowels_set:
                r -= 1
            if l < r:
                str_list[l], str_list[r] = str_list[r], str_list[l]
                l += 1
                r -= 1    

        return "".join(str_list)