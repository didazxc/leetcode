

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


def cum0(root: TreeNode):
    obj = {'num': 0}

    def fn(node: TreeNode):
        if node:
            fn(node.right)
            obj['num'] += node.val
            node.val = obj['num']
            fn(node.left)
    fn(root)
    return root


def cum1(root: TreeNode):
    num = 0
    stack = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.right
        else:
            node = stack.pop()
            num += node.val
            node.val = num
            cur = node.left
    return root


def cum(root: TreeNode):
    num = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if node.left:
                stack.append(node.left)
            stack.append(node)
            stack.append(None)
            if node.right:
                stack.append(node.right)
        else:
            node = stack.pop()
            num += node.val
            node.val = num
    return root


if __name__ == '__main__':
    r = TreeNode.apply([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
    print(r)
    print(cum(r))
