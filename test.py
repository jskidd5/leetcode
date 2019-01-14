"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.vec = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.vec.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.vec


#
# class Solution:
#     def deserialize(self, s):
#         """
#         :type s: str
#         :rtype: NestedInteger
#         """
#         res = NestedInteger()
#         tmp_nest = []
#         nums = ''
#         for i in s:
#             if i == '[':
#                 tmp_nest.append(NestedInteger())
#             elif i == ']':
#                 res.add(tmp_nest.pop())
#             elif i == ',':
#                 if nums != '':
#                     tmp_nest[-1].add(int(nums))
#                     nums = ''
#             else:
#                 nums += i
#         if nums != '':
#             res.setInteger(int(nums))
#         return res
class Solution:
    def deserialize(self, s):
        stack, num, last = [], "", None
        for c in s:
            if c.isdigit() or c == "-":
                num += c
            elif c == "," and num:
                stack[-1].add(NestedInteger(int(num)))
                num = ""
            elif c == "[":
                elem = NestedInteger()
                if stack:
                    stack[-1].add(elem)
                stack.append(elem)
            elif c == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                last = stack.pop()
        return last if last else NestedInteger(int(num))


s = Solution()
print(s.deserialize("[123,456,[788,799,833],[[]],10,[]]").getList())
