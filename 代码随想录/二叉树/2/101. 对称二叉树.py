

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


def is_symmetric0(root: TreeNode):
    stack_l = [root.left]
    stack_r = [root.right]
    while stack_l:
        node_l = stack_l.pop()
        node_r = stack_r.pop()
        if node_l is None and node_r is None:
            continue
        elif node_l is None or node_r is None:
            return False
        if node_l.val != node_r.val:
            return False
        stack_l.append(node_l.right)
        stack_l.append(node_l.left)
        stack_r.append(node_r.left)
        stack_r.append(node_r.right)
    return True


def is_symmetric(root: TreeNode):

    def compare(root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return compare(root1.left, root2.right) and compare(root1.right, root2.left)

    return compare(root.left, root.right)


if __name__ == '__main__':
    r = TreeNode.apply([1,2,2,3,4,4,3])
    print(r)
    print(is_symmetric(r))
    r = TreeNode.apply([1,2,2,None,3,None,3])
    print(r)
    print(is_symmetric(r))
