"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove(head: ListNode, n: int):
    dummy_head = ListNode(next=head)
    nth_last = dummy_head
    bottom = dummy_head
    diff = 0
    while diff < n and bottom is not None:
        bottom = bottom.next
    while bottom is not None:
        nth_last = nth_last.next
        bottom = bottom.next
    if diff == n:
        nth_last.next = nth_last.next.next
    return dummy_head.next

