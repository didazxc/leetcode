

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
            return TreeNode(nums[i], left=left, right=right) if nums[i] is not None else None

        return build(0)


def trim(root: TreeNode, low, high):
    if root is None:
        return None
    if root.val < low:
        return trim(root.right, low, high)
    if root.val > high:
        return trim(root.left, low, high)
    root.left = trim(root.left, low, high)
    root.right = trim(root.right, low, high)
    return root


def trim0(root: TreeNode, low, high):
    new_root = root
    while new_root and not(low <= new_root.val <= high):
        if low > new_root.val:
            new_root = new_root.right
        elif high < new_root.val:
            new_root = new_root.left
    if new_root is None:
        return None
    cur = new_root
    while cur.left:
        if cur.left.val >= low:
            cur = cur.left
        else:
            cur.left = cur.left.right
    cur = new_root
    while cur.right:
        if cur.right.val <= high:
            cur = cur.right
        else:
            cur.right = cur.right.left
    return new_root


if __name__ == '__main__':
    r = TreeNode.apply([3,0,4,None,2,None,None,None, None, 1])
    print(r)
    print(trim0(r,1,3))
