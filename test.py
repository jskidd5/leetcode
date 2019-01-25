# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max_cnt = 0
        res, flg = self.get_val(root, [], 0)
        if self.max_cnt > flg:
            res.pop()
        elif self.max_cnt < flg:
            res = [res[-1]]
            self.max_cnt = flg
        return res

    def get_val(self, root, res, flg):
        if root is None:
            return res, flg
        if root.left:
            res, flg = self.get_val(root.left, res, flg)
        if res:
            if root.val not in res:
                if self.max_cnt > flg:
                    res.pop()
                elif self.max_cnt < flg:
                    res = [res[-1]]
                    self.max_cnt = flg
                res.append(root.val)
                flg = 1
            else:
                flg += 1
        else:
            res.append(root.val)
            flg = 1
        if root.right:
            res, flg = self.get_val(root.right, res, flg)
        return res, flg


# p = TreeNode(6)
# p.left = TreeNode(2)
# p.left.left = TreeNode(2)
# p.left.right = TreeNode(4)
# p.left.right.left = TreeNode(3)
# p.left.right.right = TreeNode(5)
# p.right = TreeNode(8)
# p.right.left = TreeNode(8)
# p.right.right = TreeNode(9)

p = TreeNode(1)
p.right = TreeNode(2)
p.right.left = TreeNode(2)

s = Solution()
res = s.findMode(p)
print(res)
