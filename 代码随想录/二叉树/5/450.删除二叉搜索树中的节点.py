

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


def delete_root0(root: TreeNode):
    if root.right is None:
        return root.left
    cur = root.right
    while cur.left:
        cur = cur.left
    cur.left = root.left
    return root.right


def delete_root(root: TreeNode):
    if root.right is None:
        return root.left
    cur = root.right
    pre = None
    while cur.left:
        pre = cur
        cur = cur.left
    if pre is None:
        cur.left = root.left
        return root.right
    root.val = cur.val
    pre.left = None
    return root


def delete0(root: TreeNode, a):
    cur = root
    pre = None
    while cur and cur.val != a:
        pre = cur
        cur = cur.left if cur.val > a else cur.right
    if cur is None:
        return root
    if pre is None:
        return delete_root(cur)
    if pre.left and pre.left.val == a:
        pre.left = delete_root(cur)
    if pre.right and pre.right.val == a:
        pre.right = delete_root(cur)
    return root


def delete(root: TreeNode, a):
    if root.val == a:
        return delete_root(root)
    elif root.val > a:
        root.left = delete(root.left, a)
    else:
        root.right = delete(root.right, a)
    return root


if __name__ == '__main__':
    r = TreeNode.apply([5,3,6,2,4,5.5,7])
    print(r)
    print(delete(r, 5))

