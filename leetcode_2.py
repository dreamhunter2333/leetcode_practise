# -*- coding: utf-8 -*-

"""
2. 两数相加

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(a,b,carry):
            if not (a or b):
                return ListNode(1) if carry else None
            # 如果a为空则将ListNode(0)赋给a，对于b也是
            a = a if a else ListNode(0)
            b = b if b else ListNode(0)
            #处理val，以及进位标志
            val = a.val + b.val + carry
            carry = 1 if val>=10 else 0
            a.val = val%10
            # 现在a的值就是两个节点相加后的和了
            # 之后再次递归计算a.next和b.next
            a.next = add(a.next,b.next,carry)
            return a
        return add(l1,l2,0)
