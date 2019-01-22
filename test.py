# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res = True
        stack = [[p, q]]
        print(stack)
        while stack:
            root = stack.pop()
            if root[0] and root[1]:
                print(root[0].val)
                if root[0].val != root[1].val:
                    return False
                else:
                    stack.append([root[0].right, root[1].right])
                    stack.append([root[0].left, root[1].left])
            elif root[0] or root[1]:
                return False
        return res


p = TreeNode(1)
p.left = TreeNode(2)
p.left.right = TreeNode(3)
p.left.right.left = TreeNode(4)
p.right = TreeNode(5)
p.right.right = TreeNode(6)
p.right.right.left = TreeNode(7)
p.right.right.left.left = TreeNode(8)
p.right.right.left.right = TreeNode(9)

s = Solution()
print(s.isSameTree(p, p))
