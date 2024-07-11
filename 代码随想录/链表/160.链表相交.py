"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __len__(self):
        length = 1
        tmp = self
        while tmp.next is not None:
            length += 1
            tmp = tmp.next
        return length

    def next_n(self, n: int):
        cur = self
        for _ in range(n):
            assert cur is not None
            cur = cur.next
        return cur

    @staticmethod
    def apply(arr):
        last = None
        for i in range(len(arr) - 1, -1, -1):
            last = ListNode(val=arr[i], next=last)
        return last


def intersect(head1: ListNode, head2: ListNode):
    len1 = len(head1)
    len2 = len(head2)
    if len1 >= len2:
        head1 = head1.next_n(len1 - len2)
    else:
        head2 = head2.next_n(len2 - len1)
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    return head1


if __name__ == '__main__':
    list1 = ListNode.apply([4, 1, 8, 4, 5])
    list2 = ListNode.apply([5, 0, 1])
    list2.next_n(2).next = list1.next_n(2)
    inter = intersect(list1, list2)
    print(inter)
