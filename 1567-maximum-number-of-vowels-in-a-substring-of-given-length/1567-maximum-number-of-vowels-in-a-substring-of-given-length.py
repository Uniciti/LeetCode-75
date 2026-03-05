class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a','e','i','o','u')
        vow_counter = 0
        for i in range(k):
            if s[i] in vowels:
                vow_counter += 1
        max_vow = vow_counter
        for i in range(len(s) - k):
            if s[i] in vowels:
                vow_counter -= 1
            if s[i + k] in vowels:
                vow_counter += 1
            if max_vow <= vow_counter:
                max_vow = vow_counter
        return max_vow