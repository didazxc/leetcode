"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意: 你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3] 返回如下的二叉树：

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


def build(inorder: list, postorder: list):
    if not inorder or not postorder:
        return None
    root = postorder[-1]
    middle = inorder.index(root)
    left = build(inorder[:middle], postorder[:middle])
    right = build(inorder[middle+1:], postorder[middle:-1])
    return TreeNode(val=root, left=left, right=right)


def build2(preorder, inorder):
    if not inorder or not preorder:
        return None
    root = preorder[0]
    middle = inorder.index(root)
    left = build2(preorder[1:middle+1], inorder[:middle])
    right = build2(preorder[middle+1:], inorder[middle+1:])
    return TreeNode(val=root, left=left, right=right)


if __name__ == '__main__':
    r = build([9,3,15,20,7], [9,15,7,20,3])
    print(r)
    r = build2([3,9,20,15,7],[9, 3, 15, 20, 7])
    print(r)

