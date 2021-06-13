#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.val


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # 哈希
        # node_set = set()
        # node = head
        # node_set.add(head)
        # while node.next:
        #     node = node.next
        #     if node in node_set:
        #         return node
        #     node_set.add(node)
        # return None

        p = head
        q = head.next

        while p != q:
            if not p or not q or not q.next:
                return None
            p = p.next
            q = q.next.next

        if p in [head, None] or p.next == p:
            return p

        i = head
        j = p.next

        while i:
            while j != p:
                if i == j:
                    return i
                j = j.next

            i = i.next
            j = p.next

        return None


def list2node(nums, pos):
    root = ListNode(None)
    cur_node = root
    cicle_node = None
    for i in range(len(nums)):
        cur_node.next = ListNode(nums[i])
        cur_node = cur_node.next
        if i == pos:
            cicle_node = cur_node
    cur_node.next = cicle_node
    return root.next


print(Solution().detectCycle(
    list2node([-1, -7, 7, -4, 19, 6, -9, -5, -2, -5], 9)))
# @lc code=end
