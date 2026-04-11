from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        dq = deque(maxlen=len(s))
        for i in s:
            if i == '*':
                dq.pop()
            else:
                dq.append(i)

        return "".join(dq)