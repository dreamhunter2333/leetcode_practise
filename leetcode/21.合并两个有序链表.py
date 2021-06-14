#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        res = ListNode()
        head = res

        while node1 and node2:
            if node1.val < node2.val:
                res.next = node1
                res = node1
                node1 = node1.next
            else:
                res.next = node2
                res = node2
                node2 = node2.next
        res.next = node1 if node1 else node2

        return head.next

# @lc code=end
