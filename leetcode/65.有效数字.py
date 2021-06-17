#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:

        if not s:
            return False

        n = len(s)

        symbols = ['+', '-']
        nums = [str(i) for i in range(10)]
        dot = '.'
        e = ['E', 'e']

        state = 0
        for i, c in enumerate(s, 1):
            if state == 0:
                if (c in symbols and i < n and s[i] in nums+[dot]) or c in nums:
                    state = 1
                elif c == dot and i < n and s[i] in nums:
                    state = 2
                else:
                    return False
            elif state == 1:
                if c in nums:
                    continue
                elif c == dot and ((i > 1 and s[i-2] in nums) or (i < n and s[i] in nums)):
                    state = 2
                elif c in e and i < n:
                    state = 3
                else:
                    return False
            elif state == 2:
                if c in nums:
                    continue
                elif c in e and i < n:
                    state = 3
                else:
                    return False
            elif state == 3:
                if c in symbols and i < n:
                    state = 4
                elif c in nums:
                    state = 4
                else:
                    return False
            elif state == 4:
                if c in nums:
                    continue
                else:
                    return False

        return True

# @lc code=end
