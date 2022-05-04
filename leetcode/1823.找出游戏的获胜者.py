#
# @lc app=leetcode.cn id=1823 lang=python3
#
# [1823] 找出游戏的获胜者
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        data = list(range(1, n + 1))
        all_sum = n
        i = 0
        while len(data) > 1:
            i = ((i + k % all_sum) % all_sum or all_sum) - 1
            data.pop(i)
            all_sum -= 1

        return data.pop()


# print(Solution().findTheWinner(6, 5))
# @lc code=end
