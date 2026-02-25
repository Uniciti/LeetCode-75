class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        result = []
        for v in s:
            if v != " ":
                word.append(v)
            else:
                if word:
                    result.append("".join(word))
                    word.clear()

        if word:
            result.append("".join(word))
            word.clear()

        return " ".join(reversed(result))
        # return " ".join(reversed(s.split()))