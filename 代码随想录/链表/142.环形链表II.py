"""
题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    @staticmethod
    def apply(arr, idx):
        id_node = None
        last_node = None
        last = None
        for i in range(len(arr) - 1, -1, -1):
            last = ListNode(val=arr[i], next=last)
            if i == len(arr) - 1:
                last_node = last
            elif i == idx:
                id_node = last
        last_node.next = id_node
        return last


def cycle(head: ListNode):
    """
    快指针所走路程是慢指针的2倍，相遇后，慢指针所走路径(循环外)与快指针多走的路径(循环内)长度一样，相当于已经对齐了的两个链表求叫交点
    """
    fast = head
    slow = head
    while slow.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            intersect = head
            while intersect != slow:
                intersect = intersect.next
                slow = slow.next
            return intersect
    return None


if __name__ == '__main__':
    print(cycle(ListNode.apply([3,2,0,-4], -1)))
