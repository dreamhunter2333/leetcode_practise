#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        value = [[None, "Buzz"], ["Fizz", "FizzBuzz"]]

        def print_val(num):
            flag1 = num % 3 == 0
            flag2 = num % 5 == 0
            if flag1 or flag2:
                return value[flag1][flag2]
            return str(num)

        res = []
        for i in range(n):
            res.append(print_val(i+1))

        return res
# @lc code=end
