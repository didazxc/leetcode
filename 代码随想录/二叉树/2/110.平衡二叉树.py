"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

110.平衡二叉树

返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

110.平衡二叉树1

返回 false 。
"""


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


def is_balance0(root: TreeNode):

    def get_depth(node: TreeNode) -> int:
        if node is None:
            return 0
        left = get_depth(node.left)
        right = get_depth(node.right)
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return get_depth(root) != -1


def is_balance(root: TreeNode):
    stack = [root]
    h_map = {}
    while stack:
        node = stack.pop()
        if node:
            stack.append(node)
            stack.append(None)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        else:
            node = stack.pop()
            left = h_map.get(node.left, 0)
            right = h_map.get(node.right, 0)
            if abs(left - right) > 1:
                return False
            h_map[node] = max(left, right) + 1
    return True


if __name__ == '__main__':
    r = TreeNode.apply([3,9,20,None,None,15,7])
    print(r)
    print(is_balance(r))
    r = TreeNode.apply([1,2,2,3,3,None,None,4,4])
    print(r)
    print(is_balance(r))
