#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return s
        stack = []
        for item in s:
            if item == ')':
                cur_items = []
                while stack and stack[-1] != '(':
                    cur_items.append(stack.pop())
                stack.pop()
                stack.extend(cur_items)
            else:
                stack.append(item)
        return ''.join(stack)

# @lc code=end
