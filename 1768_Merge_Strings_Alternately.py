class Solution:
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     result = []
    #     i = 0
    #     while i < len(word1) or i < len(word2):
    #         if  i < len(word1):
    #             result.append(word1[i])
    #         if  i < len(word2):
    #             result.append(word2[i])
    #         i += 1
    #     return "".join(result)
    
    # -> Это интереснее <-
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(min(len(word1), len(word2))):
            result.append(word1[i])
            result.append(word2[i])
        if len(word1) > len(word2):
            result.append(word1[len(word2):])
        if len(word2) > len(word1):
            result.append(word2[len(word1):])
        return "".join(result)
    
print(Solution.mergeAlternately(Solution, "qwerty", "asd"))

