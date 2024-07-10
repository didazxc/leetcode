"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        a = []
        cur = self
        while cur is not None:
            a.append(cur.val)
            cur = cur.next
        return str(a)

    @staticmethod
    def apply(arr):
        last = None
        for i in range(len(arr)-1, -1, -1):
            last = ListNode(val=arr[i], next=last)
        return last


def swap(head: ListNode):
    a = head.next
    b = a.next
    a.next = b.next
    b.next = a
    head.next = b
    return a


def swap_list(head: ListNode):
    new_head = ListNode(next=head)
    cur = new_head
    while cur.next is not None and cur.next.next is not None:
        cur = swap(cur)
    return new_head.next or []


if __name__ == '__main__':
    list_node = ListNode.apply([1,2,3,4,5])
    print(swap_list(list_node))
