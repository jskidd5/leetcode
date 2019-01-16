class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == '(':
                stack.append(-1)
            elif s == ')':
                tmp = 0
                while stack and stack[-1] != -1:
                    tmp += stack.pop()
                stack.pop()
                if tmp:
                    stack.append(2 * tmp)
                else:
                    stack.append(1)
        return sum(stack)


s = Solution()
print(s.scoreOfParentheses('()()'))
