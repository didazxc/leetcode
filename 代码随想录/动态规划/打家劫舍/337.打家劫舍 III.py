"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(root: TreeNode):
    if root is None:
        return 0, 0
    s1 = traversal(root.left)
    s2 = traversal(root.right)
    v0 = max(s1[0], s1[1]) + max(s2[0], s2[1])
    v1 = s1[0] + s2[0] + root.val
    return v0, v1


def rob(root: TreeNode):
    return max(traversal(root))

