#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_map = {}

        def find_node(target_node):
            if target_node is None:
                return None
            if target_node not in node_map:
                node_map[target_node] = Node(target_node.val)
            return node_map[target_node]

        root = Node(0)
        new_node = root
        node = head
        while node:
            temp = find_node(node)
            temp.random = find_node(node.random)
            new_node.next = temp
            node = node.next
            new_node = new_node.next

        return root.next

# @lc code=end
