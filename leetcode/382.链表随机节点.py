#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

# @lc code=start
# Definition for singly-linked list.
from random import randint
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.cache = []
        root = head
        while root:
            self.cache.append(root.val)
            root = root.next
        self.len = len(self.cache)

    def getRandom(self) -> int:
        return self.cache[randint(0, self.len - 1)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
