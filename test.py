# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root, -1]]
        left_stack = []
        right_stack = []
        res = 0
        pre = root
        while len(stack) > 0:
            while (len(stack) > 0 and (stack[-1][0].right is None and stack[-1][0].left is None) or
                   (len(stack) > 0 and (stack[-1][0].left == pre or stack[-1][0].right == pre))):
                if stack[-1][0].right is None and stack[-1][0].left is None:
                    if stack[-1][1] == 1:
                        left_stack.append(stack[-1][0].val)
                    elif stack[-1][1] == 0:
                        right_stack.append(stack[-1][0].val)
                else:
                    tmp_l = 0
                    tmp_r = 0
                    if stack[-1][0].left:
                        tmp_l = left_stack.pop()
                    if stack[-1][0].right:
                        tmp_r = right_stack.pop()
                    res += abs(tmp_l - tmp_r)
                    if stack[-1][1] == 1:
                        left_stack.append(stack[-1][0].val + tmp_l + tmp_r)
                    elif stack[-1][1] == 0:
                        right_stack.append(stack[-1][0].val + tmp_l + tmp_r)
                pre = stack.pop()[0]
            if len(stack) > 0:
                tmp = stack[-1][0]
                if tmp.right:
                    stack.append([tmp.right, 0])
                if tmp.left:
                    stack.append([tmp.left, 1])
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
res = s.findTilt(p)
print(res)
