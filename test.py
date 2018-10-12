class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = [0]
        len_ops = len(ops)
        if len_ops == 0:
            return 0
        for i in range(len_ops):
            if ops[i] == 'C':
                res.pop()
            elif ops[i] == 'D':
                res.append(res[-1] + res[-1])
            elif ops[i] == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(ops[i]))
        return sum(res)


s = Solution()
print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
