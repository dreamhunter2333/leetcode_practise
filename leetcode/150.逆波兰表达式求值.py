#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for num in tokens:
            if num == '+':
                res.append(res.pop() + res.pop())
            elif num == '-':
                num2 = res.pop()
                num1 = res.pop()
                res.append(num1 - num2)
            elif num == '/':
                num2 = res.pop()
                num1 = res.pop()
                res.append(int(num1 / num2))
            elif num == '*':
                num2 = res.pop()
                num1 = res.pop()
                res.append(num1 * num2)
            else:
                res.append(int(num))

        return res[0]

# @lc code=end
