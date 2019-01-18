class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in reversed(tokens):
            try:
                stack.append(int(t))
            except ValueError:
                stack.append(t)
            while len(stack) >= 3 and isinstance(stack[-1], int) and isinstance(stack[-2], int) and isinstance(stack[-3], str):
                tmp = int(eval(str(stack[-1]) + stack[-3] + str(stack[-2])))
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(tmp)
        return stack[-1]

s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
