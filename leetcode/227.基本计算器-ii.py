#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        opt = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                opt.append(s[i])
                i += 1
            elif s[i] == ')':
                while opt:
                    pre_opt = opt.pop()
                    if pre_opt == '(':
                        break
                    nums.append(pre_opt)
                i += 1
            elif s[i] in ('+', '-'):
                while opt and opt[-1] != '(':
                    nums.append(opt.pop())
                opt.append(s[i])
                i += 1
            elif s[i] in ('*', '/'):
                while opt and opt[-1] in ('*', '/'):
                    nums.append(opt.pop())
                opt.append(s[i])
                i += 1
            else:
                num = ''
                while i < len(s) and s[i] == ' ':
                    i += 1
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                if num:
                    nums.append(int(num))

        while opt:
            nums.append(opt.pop())

        res = []

        for num in nums:
            if num == '+':
                res.append(res.pop() + res.pop())
            elif num == '-':
                num2 = res.pop()
                num1 = res.pop()
                res.append(num1 - num2)
            elif num == '/':
                num2 = res.pop()
                num1 = res.pop()
                res.append(num1 // num2)
            elif num == '*':
                num2 = res.pop()
                num1 = res.pop()
                res.append(num1 * num2)
            else:
                res.append(num)

        return res[0]

# @lc code=end
