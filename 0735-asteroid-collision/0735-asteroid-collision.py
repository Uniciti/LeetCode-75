class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        aster_stack = []
        for x in asteroids:
            if x > 0:
                aster_stack.append(x)
            else:
                while not aster_stack or aster_stack[-1] < x*-1:
                    if not aster_stack or aster_stack[-1] < 0:
                        break;
                    aster_stack.pop()
                if not aster_stack:
                    aster_stack.append(x)
                elif aster_stack[-1] < x*-1:
                    aster_stack.append(x)
                elif aster_stack[-1] == x*-1:
                    aster_stack.pop()

        return aster_stack