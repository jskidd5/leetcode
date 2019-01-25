# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        stack = [root]
        res = 0
        while stack:
            tmp = stack.pop()
            res += self.path_val(tmp, sum)
            if tmp and tmp.left:
                stack.append(tmp.left)
            if tmp and tmp.right:
                stack.append(tmp.right)
        return res

    def path_val(self, root, sum):
        if root is None:
            return 0
        cnt = 0
        val = 0
        high = 0
        nums = []
        stack = [[root, high + 1, nums]]
        while stack:
            tmp = stack.pop()
            while high >= tmp[1]:
                val -= tmp[2].pop()
                high -= 1
            tmp[2].append(tmp[0].val)
            val += tmp[0].val
            if val == sum:
                cnt += 1
            if tmp[0].right:
                stack.append([tmp[0].right, tmp[1] + 1, tmp[2]])
            if tmp[0].left:
                stack.append([tmp[0].left, tmp[1] + 1, tmp[2]])
            high += 1
        return cnt


p = TreeNode(6)
p.left = TreeNode(2)
p.left.left = TreeNode(0)
p.left.right = TreeNode(4)
p.left.right.left = TreeNode(3)
p.left.right.right = TreeNode(5)
p.right = TreeNode(8)
p.right.left = TreeNode(7)
p.right.left.left = TreeNode(-4)
p.right.right = TreeNode(9)
p.right.right.left = TreeNode(2)
s = Solution()
res = s.pathSum(p, 11)
res = s.pathSum(p, 11)
print(res)
