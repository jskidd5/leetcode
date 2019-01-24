# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack_p = [root]
        stack_q = [root]
        tmp = root
        while tmp and p.val != tmp.val:
            if tmp and tmp.val > p.val:
                tmp = tmp.left
                stack_p.append(tmp)
            elif tmp and tmp.val < p.val:
                tmp = tmp.right
                stack_p.append(tmp)
        tmp = root
        while tmp and q.val != tmp.val:
            if tmp and tmp.val > q.val:
                tmp = tmp.left
                stack_q.append(tmp)
            elif tmp and tmp.val < q.val:
                tmp = tmp.right
                stack_q.append(tmp)
        while len(stack_p) > len(stack_q):
            stack_p.pop()
        while len(stack_p) < len(stack_q):
            stack_q.pop()
        while stack_p[-1].val != stack_q[-1].val:
            stack_p.pop()
            stack_q.pop()
        return stack_p[-1]


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
res = s.lowestCommonAncestor(p, TreeNode(2), TreeNode(4))
print(res.val)
