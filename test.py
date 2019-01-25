# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        p = root
        stack = []
        vals = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                tmp = stack.pop()
                if tmp.val not in vals:
                    vals.append(tmp.val)
                p = tmp.right
        print(vals)
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                tmp = stack.pop()
                start = vals.index(tmp.val)
                tmp.val = sum(vals[start:])
                p = tmp.right
        p = root
        stack = []
        vals = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                tmp = stack.pop()
                vals.append(tmp.val)
                p = tmp.right
        return vals



p = TreeNode(6)
p.left = TreeNode(2)
p.left.left = TreeNode(2)
p.left.right = TreeNode(4)
p.left.right.left = TreeNode(3)
p.left.right.right = TreeNode(5)
p.right = TreeNode(8)
p.right.left = TreeNode(8)
p.right.right = TreeNode(9)

# p = TreeNode(5)
# p.left = TreeNode(2)
# p.right = TreeNode(13)

s = Solution()
res = s.convertBST(p)
print(res)
