class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'TreeNode':
        if root is None:
            return None
        pre_root = TreeNode(0)
        stack = [[root, pre_root]]
        while len(stack) > 0:
            curr, parent = stack.pop()
            if curr.val < L:
                if curr.right:
                    parent.left = curr.right
                    stack.append([curr.right, parent])
                else:
                    parent.left = None
            elif curr.val > R:
                if curr.left:
                    parent.right = curr.left
                    stack.append([curr.left, parent])
                else:
                    parent.right = None
            else:
                print(curr.val)
                if curr.right:
                    stack.append([curr.right, curr])
                if curr.left:
                    stack.append([curr.left, curr])
        if pre_root.left and L <= pre_root.left.val <= R:
            return pre_root.left
        elif pre_root.right:
            return pre_root.right
        else:
            return root


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    root = stringToTreeNode('[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]')
    L = 25
    R = 26

    ret = Solution().trimBST(root, L, R)

    out = treeNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
