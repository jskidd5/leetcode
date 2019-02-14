# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        stack = [root]
        tmp_list = []
        if root is None:
            return False
        curr = stack[-1].left
        while len(stack) > 0:
            if curr and stack[-1].left:
                stack.append(stack[-1].left)
            else:
                tmp = stack.pop()
                tmp_list.append(tmp.val)
                if tmp.right:
                    stack.append(tmp.right)
                curr = tmp.right
        l = 0
        r = len(tmp_list) - 1
        while l < r:
            if tmp_list[l] + tmp_list[r] == k:
                return True
            elif tmp_list[l] + tmp_list[r] < k:
                l += 1
            else:
                r -= 1
        return False


p = TreeNode(6)
p.left = TreeNode(2)
p.left.left = TreeNode(1)
p.left.right = TreeNode(4)
p.left.right.left = TreeNode(3)
p.left.right.right = TreeNode(5)
p.right = TreeNode(8)
p.right.left = TreeNode(7)
p.right.right = TreeNode(9)

t = TreeNode(5)
t.left = TreeNode(2)
t.left.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.left.left = TreeNode(1)
s = Solution()
res = s.findTarget(p,30)
print(res)
