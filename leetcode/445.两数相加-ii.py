#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 反转链表
        head1 = ListNode()
        cur = l1
        while cur:
            node = cur.next
            cur.next = head1.next
            head1.next = cur
            cur = node
        head2 = ListNode()
        cur = l2
        while cur:
            node = cur.next
            cur.next = head2.next
            head2.next = cur
            cur = node

        res = ListNode()
        node1 = head1.next
        node2 = head2.next
        delta = 0

        while node1 or node2 or delta:
            cur_val = (
                (node1.val if node1 else 0) +
                (node2.val if node2 else 0) +
                delta
            )
            delta = cur_val // 10
            cur = ListNode(
                cur_val % 10,
                res.next
            )
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
            res.next = cur

        return res.next


# @lc code=end
def node_2_list(node: ListNode):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


def list_2_node(val_list: list):
    res = ListNode()
    node = res
    for val in val_list:
        cur = ListNode(val)
        node.next = cur
        node = cur
    return res.next


print(node_2_list(Solution().addTwoNumbers(
    list_2_node([7, 2, 4, 3]),
    list_2_node([5, 6, 4]),
)))
print(node_2_list(Solution().addTwoNumbers(
    list_2_node([2, 4, 3]),
    list_2_node([5, 6, 4]),
)))
print(node_2_list(Solution().addTwoNumbers(
    list_2_node([5]),
    list_2_node([5]),
)))
