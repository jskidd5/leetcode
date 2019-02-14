# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        res = str(t.val)
        stack = [[t, 0]]
        last_h = -1
        pair = 0
        while t and len(stack) > 0:
            tmp = stack.pop()
            if last_h > tmp[1]:
                cnt = last_h - tmp[1]
                while pair and cnt:
                    res += ')'
                    pair -= 1
                    cnt -= 1
            if tmp[1] > 0:
                res += '(' + str(tmp[0].val)
                pair += 1
            if tmp[0].right is None and tmp[0].left is None:
                res += ')'
                pair -= 1
            elif tmp[0].left is None:
                res += '()'
            last_h = tmp[1]
            if tmp[0].right:
                stack.append([tmp[0].right, tmp[1] + 1])
            if tmp[0].left:
                stack.append([tmp[0].left, tmp[1] + 1])
        if pair > 0:
            while pair:
                res += ')'
                pair -= 1
        else:
            res = res[0:len(res) + pair]
        return res


p = TreeNode(6)
p.left = TreeNode(2)
p.left.left = TreeNode(1)
p.left.right = TreeNode(4)
p.left.right.left = TreeNode(3)
p.left.right.right = TreeNode(5)
p.right = TreeNode(8)
p.right.left = TreeNode(7)
p.right.right = TreeNode(9)

t = TreeNode(5)
t.left = TreeNode(2)
t.left.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.left.left = TreeNode(1)
s = Solution()
res = s.tree2str(t)
print(res)
