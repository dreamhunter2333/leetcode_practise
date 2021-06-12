#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        new_head = head
        node = head

        while node.next:
            next_node = node.next
            next_next_node = node.next.next

            node.next = next_next_node
            next_node.next = new_head
            new_head = next_node

        return new_head

# @lc code=end
