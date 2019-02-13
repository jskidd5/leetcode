# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None or t is None:
            return False
        root = s
        cmp = []
        stack = [root]
        while stack and stack[-1]:
            tmp = stack.pop()
            if tmp.val == t.val:
                cmp.append(tmp)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        if len(cmp) == 0:
            return False

        for c in cmp:
            res = True
            stack = [[c, t]]
            while stack and stack[-1]:
                tmp = stack.pop()
                if tmp[0].val != tmp[1].val:
                    res = False
                    break
                if tmp[0].right and tmp[1].right:
                    stack.append([tmp[0].right, tmp[1].right])
                elif (tmp[0].right is None and tmp[1].right) or (tmp[0].right and tmp[1].right is None):
                    res = False
                    break
                if tmp[0].left and tmp[1].left:
                    stack.append([tmp[0].left, tmp[1].left])
                elif (tmp[0].left is None and tmp[1].left) or (tmp[0].left and tmp[1].left is None):
                    res = False
                    break
            if res:
                return True
        return res


p = TreeNode(2)
p.left = TreeNode(2)
p.left.left = TreeNode(2)
# p.left.right = TreeNode(4)
# p.left.right.left = TreeNode(3)
# p.left.right.right = TreeNode(5)
# p.right = TreeNode(8)
# p.right.left = TreeNode(7)
# p.right.right = TreeNode(9)

t = TreeNode(1)

s = Solution()
res = s.isSubtree(p, t)
print(res)
