

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


def insert0(root: TreeNode, a):
    pre = None
    cur = root
    while cur:
        if cur.val > a:
            pre = cur
            cur = cur.left
        elif cur.val < a:
            pre = cur
            cur = cur.right
    else:
        if pre.val > a:
            pre.left = TreeNode(a)
        else:
            pre.right = TreeNode(a)
    return root


def insert(root: TreeNode, a):
    if root is None:
        return TreeNode(a)
    if root.val > a:
        root.left = insert(root.left, a)
    elif root.val < a:
        root.right = insert(root.right, a)
    return root


if __name__ == '__main__':
    r = TreeNode.apply([4,2,7,1,3])
    print(r)
    print(insert(r, 5))
