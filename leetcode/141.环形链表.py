#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        p = head
        q = head.next
        while p != q:
            p = p.next if p else None
            q = q.next.next if q and q.next else None

        return p is not None

# @lc code=end
