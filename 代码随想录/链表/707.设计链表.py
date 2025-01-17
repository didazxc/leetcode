"""
在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index):
        if index >= self.size or index < 0:
            return -1
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        return cur.next.val

    def addAtHead(self, val):
        self.size += 1
        self.dummy_head.next = ListNode(val=val, next=self.dummy_head.next)

    def addAtTail(self, val):
        self.size += 1
        cur = self.dummy_head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val=val)

    def addAtIndex(self, index, val):
        if index >= self.size:
            return
        if index < 0:
            self.addAtHead(val)
        elif index == self.size - 1:
            self.addAtTail(val)
        else:
            cur = self.dummy_head
            for _ in range(index):
                cur = cur.next
            cur.next = ListNode(val=val, next=cur.next)
        self.size += 1

    def deleteAtIndex(self, index):
        if self.size > index >= 0:
            self.size -= 1
            cur = self.dummy_head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next

