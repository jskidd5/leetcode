# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            t1 = TreeNode(0)
        if t2 is None:
            t2 = TreeNode(0)
        stack = [[t1, t2]]
        while len(stack) > 0:
            tmp = stack.pop()
            tmp[0].val += tmp[1].val
            if tmp[0].right or tmp[1].right:
                if tmp[0].right is None:
                    tmp[0].right = TreeNode(0)
                if tmp[1].right is None:
                    tmp[1].right = TreeNode(0)
                stack.append([tmp[0].right, tmp[1].right])
            if tmp[0].left or tmp[1].left:
                if tmp[0].left is None:
                    tmp[0].left = TreeNode(0)
                if tmp[1].left is None:
                    tmp[1].left = TreeNode(0)
                stack.append([tmp[0].left, tmp[1].left])
        return t1


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
res = s.mergeTrees(p, t)
print(res)
