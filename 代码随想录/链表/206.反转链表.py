"""
题意：反转一个单链表。

示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: ListNode):
    last = None
    cur = head
    while cur is not None:
        tmp = cur.next
        cur.next = last
        last = cur
        cur = tmp
    return last


def reverse1(head: ListNode):
    def fn(last, cur):
        tmp = cur.next
        cur.next = last
        fn(cur, tmp)
    fn(None, head)


def reverse2(head: ListNode):
    if head is None:
        return None
    if head.next is None:
        return head
    last = reverse2(head.next)
    head.next = None
    head.next.next = head
    return last

