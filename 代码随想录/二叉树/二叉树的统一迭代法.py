

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def apply(nums):
        n = len(nums)

        def build(i):
            left = build(2*i+1) if 2*i+1 < n else None
            right = build(2*i+2) if 2*i+2 < n else None
            return TreeNode(nums[i], left=left, right=right) if nums[i] else None

        return build(0)


def preorder(root: TreeNode):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            stack.append(node)
            stack.append(None)
        else:
            res.append(stack.pop().val)
    return res


def inorder(root: TreeNode):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            stack.append(None)
            if node.left:
                stack.append(node.left)
        else:
            res.append(stack.pop().val)
    return res


def postorder(root: TreeNode):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            stack.append(node)
            stack.append(None)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        else:
            res.append(stack.pop().val)
    return res


if __name__ == '__main__':
    r = TreeNode.apply([5, 4, 6, 1, 2])
    print(preorder(r))
    print(inorder(r))
    print(postorder(r))

