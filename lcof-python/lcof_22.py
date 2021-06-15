"""
剑指 Offer 22. 链表中倒数第k个节点
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        res = head

        while head:
            if k > 0:
                k -= 1
            else:
                res = res.next
            head = head.next

        return res
