class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        impact = False
        distroy = False
        for a in asteroids:
            while len(stack) > 0 and impact:
                if stack[-1] < 0:
                    impact = False
                elif a < 0:
                    if stack[-1] + a > 0:
                        distroy = True
                        impact = False
                    elif stack[-1] + a < 0:
                        stack.pop()
                    else:
                        stack.pop()
                        distroy = True
                        impact = False
                elif a > 0:
                    impact = False
            if not distroy:
                stack.append(a)
            impact = True
            distroy = False
        return stack


s = Solution()
print(s.asteroidCollision([10, 2, -5]))
