#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list2node(vals: list) -> 'ListNode':
        pre_node = None
        for val in reversed(vals):
            pre_node = ListNode(val=val, next=pre_node)
        return pre_node

    def __repr__(self) -> str:
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
        return str(res)


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        root = ListNode(next=head)
        cur_node = root
        pre_node = root

        i = left
        while left > 0:
            pre_node = cur_node
            cur_node = cur_node.next
            left -= 1

        while i < right:
            i += 1
            next_node = cur_node.next
            next_next_node = cur_node.next.next

            cur_node.next = next_next_node
            next_node.next = pre_node.next
            pre_node.next = next_node

        return root.next


print(Solution().reverseBetween(
    head=ListNode.list2node([3, 5]),
    left=1,
    right=2
))
# @lc code=end
