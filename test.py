class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        for t in reversed(T):
            if len(stack) == 0:
                stack.append([t, 1])
                res.append(0)
            else:
                cnt = 1
                while stack and stack[-1][0] <= t:
                    cnt += stack.pop()[1]
                if len(stack) > 0:
                    res.append(cnt)
                else:
                    res.append(0)
                stack.append([t, cnt])
            print(stack)
        res.reverse()
        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
