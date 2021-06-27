#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        cache = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in cache:
                if not stack or stack[-1] != cache[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

# @lc code=end
