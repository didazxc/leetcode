

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_lines(self):
        ls, llen, _, lpad = self.left.get_lines() if self.left else ([], 0, 0, 0)
        rs, rlen, rpad, _ = self.right.get_lines() if self.right else ([], 0, 0, 0)
        line_num = max(len(ls), len(rs))
        ls += [' ' * llen] * (line_num - len(ls))
        rs += [' ' * rlen] * (line_num - len(rs))
        val_len = len(str(self.val))
        lines = [ls[i] + ' ' * (val_len + 2) + rs[i] for i in range(line_num)]
        first_line = [f'{" "*llen} {self.val} {" "*rlen}']
        second_line = [(lpad if llen else ' '*llen) + ' ' * (val_len+2) + (rpad if rlen else ' '*rlen)]
        length = llen + val_len + 2 + rlen
        return first_line + second_line + lines, length, ' '*llen + '\\' + ' '*(length-llen-1), ' '*(llen+1+val_len)+'/'+' '*rlen

    def __str__(self):
        lines, *_ = self.get_lines()
        return '\n'.join(lines)

    @staticmethod
    def apply(nums):
        n = len(nums)

        def build(i):
            left = build(2*i+1) if 2*i+1 < n else None
            right = build(2*i+2) if 2*i+2 < n else None
            return TreeNode(nums[i], left=left, right=right) if nums[i] else None

        return build(0)


def invert(root: TreeNode):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
    return root


def inv1(root: TreeNode):
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
            node = stack.pop()
            node.left, node.right = node.right, node.left


def inv2(root: TreeNode):
    stack = [root]
    while stack:
        for i in range(len(stack)):
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left


if __name__ == '__main__':
    # r = TreeNode.apply([3, 9, 20, None, None, 15, 7])
    r = TreeNode.apply([4, 2, 7, 1, 3, 6, 9])
    inv2(r)
    print(r)

