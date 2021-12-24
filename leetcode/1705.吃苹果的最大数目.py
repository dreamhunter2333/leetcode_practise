#
# @lc app=leetcode.cn id=1705 lang=python3
#
# [1705] 吃苹果的最大数目
#

# @lc code=start
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        data_len = len(apples)
        apple_stack = {}
        apple_min = []
        count = 0
        i = -1
        while i < data_len or len(apple_min):
            i += 1
            if i < data_len and apples[i] != 0:
                day = i + days[i]
                if apple_stack.get(day):
                    apple_stack[day] += apples[i]
                else:
                    apple_stack[day] = apples[i]
                    apple_min.append(day)
                    apple_min.sort()
            while len(apple_min):
                day = apple_min[0]
                if day <= i:
                    apple_min.pop(0)
                    continue
                apple_stack[day] -= 1
                count += 1
                if apple_stack[day] == 0:
                    apple_min.pop(0)
                break

        return count


# print(Solution().eatenApples(
#     apples=[3, 0, 0, 0, 0, 2],
#     days=[3, 0, 0, 0, 0, 2]
# ))
# @lc code=end
