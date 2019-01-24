# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        stack = [root]
        while len(stack) > 0:
            tmp = stack.pop()
            if tmp and tmp.left:
                stack.append(tmp.left)
                if tmp.left.left is None and tmp.left.right is None:
                    res += tmp.left.val
            if tmp and tmp.right:
                stack.append(tmp.right)
        return res


p = TreeNode(6)
p.left = TreeNode(2)
p.left.left = TreeNode(0)
p.left.right = TreeNode(4)
p.left.right.left = TreeNode(3)
p.left.right.right = TreeNode(5)
p.right = TreeNode(8)
p.right.left = TreeNode(7)
p.right.right = TreeNode(9)

# p.right.right.left.right = TreeNode(9)

s = Solution()
res = s.sumOfLeftLeaves(p)
print(res)
