class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        len_push = len(pushed)
        push_cnt = 0
        while push_cnt < len_push:
            stack.append(pushed[push_cnt])
            push_cnt += 1
            while stack and stack[-1] == popped[0]:
                popped.pop(0)
                stack.pop()
        return len(popped) == 0


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 1, 2]))
