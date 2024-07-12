"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
解释：例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。
"""


def del_duplicate(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)


def removeDuplicates(s: str) -> str:
    res = list(s)
    slow = fast = 0
    length = len(res)

    while fast < length:
        # 如果一样直接换，不一样会把后面的填在slow的位置
        res[slow] = res[fast]

        # 如果发现和前一个一样，就退一格指针
        if slow > 0 and res[slow] == res[slow - 1]:
            slow -= 1
        else:
            slow += 1
        fast += 1

    return ''.join(res[0: slow])

