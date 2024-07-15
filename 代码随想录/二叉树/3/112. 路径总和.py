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


def sum_target10(root: TreeNode, target: int):

    def fn(node: TreeNode):
        if node is None:
            return []
        paths = fn(node.left) + fn(node.right)
        return [[node.val]+i for i in paths] if paths else [[node.val]]

    return [i for i in fn(root) if sum(i) == target]


def sum_target00(root: TreeNode, target: int):

    def fn(node: TreeNode, tg: int):
        if node is None:
            return tg == 0
        return fn(node.left, tg-node.val) or fn(node.right, tg-node.val)

    return fn(root, target)


def sum_target01(root: TreeNode, target: int):

    stack = [(root, target - root.val)]
    while stack:
        node, s = stack.pop()
        if node.left is None and node.right is None and s == 0:
            return True
        if s >= 0:
            if node.left:
                stack.append((node.left, s - node.left.val))
            if node.right:
                stack.append((node.right, s - node.right.val))
    return False


def sum_target11(root: TreeNode, target: int):
    res = []
    stack = [(root, [root.val])]
    while stack:
        node, s = stack.pop()
        if node.left is None and node.right is None and sum(s) == target:
            res.append(s)
        else:
            if node.left:
                stack.append((node.left, s + [node.left.val]))
            if node.right:
                stack.append((node.right, s + [node.right.val]))
    return res


if __name__ == '__main__':
    r = TreeNode.apply([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
    print(r)
    print(sum_target11(r, 22))

