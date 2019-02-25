class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        node_x = None
        node_y = None
        stack = [[root, None, 0]]
        if root.right:
            stack.append([root.right, root, 1])
        if root.left:
            stack.append([root.left, root, 1])
        while len(stack) > 0:
            curr = stack.pop()
            if curr[0].val == x:
                node_x = curr
            if curr[0].val == y:
                node_y = curr
            if curr[0].right:
                stack.append([curr[0].right, curr[0], curr[2] + 1])
            if curr[0].left:
                stack.append([curr[0].left, curr[0], curr[2] + 1])
        return node_x[1] != node_y[1] and node_x[2] == node_y[2]


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
    root = stringToTreeNode('[1,2,3,null,4,null,5]')

    ret = Solution().isCousins(root, 5, 4)

    # out = treeNodeToString(ret)
    out = ret
    print(out)


if __name__ == '__main__':
    main()
