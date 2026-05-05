from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        rad = 0
        dir = 0
        cur_rad = 0
        cur_dir = 0
        for c in senate:
            if c == "R":
                rad += 1
            else:
                dir += 1
            q.append(c)
        
        while rad != 0 and dir != 0:
            for _ in range(len(q)):
                flag = q.popleft()
                if flag == "R":
                    if cur_dir == 0:
                        cur_rad += 1
                        q.append(flag)
                    else:
                        cur_dir -= 1
                        rad -= 1
                else:
                    if cur_rad == 0:
                        cur_dir += 1
                        q.append(flag)
                    else:
                        cur_rad -= 1
                        dir -= 1
                # print(q, flag, rad, cur_rad, dir, cur_dir)
            
        
        if q.popleft() == "R" :
            return "Radiant"
        else:
            return "Dire"