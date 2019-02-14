# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        stack = [[root, 0]]
        map_res = {}
        res = []
        if root is None:
            return res
        curr = stack[-1][0].left
        while len(stack) > 0:
            if curr and stack[-1][0].left:
                stack.append([stack[-1][0].left, stack[-1][1] + 1])
            else:
                tmp = stack.pop()
                print(tmp[0].val, tmp[1])
                if tmp[1] in map_res:
                    map_res[tmp[1]][0] += tmp[0].val
                    map_res[tmp[1]][1] += 1
                else:
                    map_res[tmp[1]] = [tmp[0].val, 1]
                if tmp[0].right:
                    stack.append([tmp[0].right, tmp[1] + 1])
                curr = tmp[0].right
        res = len(map_res) * [0]
        for i in map_res:
            res[i] = map_res[i][0] / map_res[i][1]
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

t = TreeNode(5)
t.left = TreeNode(2)
t.left.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.left.left = TreeNode(1)
s = Solution()
res = s.averageOfLevels(p)
print(res)
