

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
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def inorder(root: TreeNode):
    res = []
    stack = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


def postorder(root: TreeNode):
    res = []
    stack = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)  # 插入stack表示已经遍历过左节点
            cur = cur.left
        else:
            cur = stack[-1]
            if cur:
                stack.append(None)  # 插入None表示左右节点都已经遍历过了
                cur = cur.right
            else:  # 左右子节点都遍历过后，处理当前节点
                stack.pop()
                res.append(stack.pop().val)
    return res


if __name__ == '__main__':
    r = TreeNode.apply([5, 4, 6, 1, 2])
    print(preorder(r))
    print(inorder(r))
    print(postorder(r))

