# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root, -1]]
        pre = root
        left_len = []
        right_len = []
        res = 0
        if root is None:
            return 0
        while stack:
            curr = stack[-1][0]
            dir = stack[-1][1]
            if stack and ((curr.left is None and curr.right is None) or
                          (curr.left == pre or curr.right == pre)):
                stack.pop()
                if curr.left is None and curr.right is None:
                    if dir:
                        left_len.append(1)
                    else:
                        right_len.append(1)
                if curr.left == pre or curr.right == pre:
                    tmp_l = 0
                    tmp_r = 0
                    if curr.left:
                        tmp_l = left_len.pop()
                    if curr.right:
                        tmp_r = right_len.pop()
                    if tmp_l > tmp_r:
                        tmp = tmp_l
                    else:
                        tmp = tmp_r
                    if dir:
                        left_len.append(tmp + 1)
                    else:
                        right_len.append(tmp + 1)
                    if res < tmp_l + tmp_r:
                        res = tmp_l + tmp_r
                pre = curr
            else:
                if curr.right:
                    stack.append([curr.right, 0])
                if curr.left:
                    stack.append([curr.left, 1])
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

# p = TreeNode(5)
# p.left = TreeNode(2)
# p.right = TreeNode(13)

s = Solution()
res = s.diameterOfBinaryTree(p)
print(res)
