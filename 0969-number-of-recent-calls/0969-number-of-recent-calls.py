from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.t_max = 3000

    def ping(self, t: int) -> int:
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)