# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        if root:
            stack.append(root)
        while stack:
            r = stack.pop()
            r.right, r.left = r.left, r.right
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)
        return root


p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
p.right = TreeNode(5)
p.right.right = TreeNode(6)
p.right.right.left = TreeNode(7)
p.right.right.right = TreeNode(8)
#p.right.right.left.right = TreeNode(9)

s = Solution()
print()
res = s.invertTree(p)
stack = [res]
while stack:
    r = stack.pop()
    print(r.val)
    if r.right:
        stack.append(r.right)
    if r.left:
        stack.append(r.left)