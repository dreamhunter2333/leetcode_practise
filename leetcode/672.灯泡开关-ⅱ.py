#
# @lc app=leetcode.cn id=672 lang=python3
#
# [672] 灯泡开关 Ⅱ
#

# @lc code=start
from typing import List, Set


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        status_set: Set[str] = set()
        reverse_map = {"0": "1", "1": "0"}

        def flag1(num): return True
        def flag2(num): return (num+1) % 2 == 0
        def flag3(num): return (num+1) % 2 == 1
        def flag4(num): return (num+1) % 3 == 1

        flag_arr = [flag1, flag2, flag3, flag4]

        def button(ttype: int, stat: List[str]):
            for i in range(n):
                if flag_arr[ttype](i):
                    stat[i] = reverse_map[stat[i]]

        for i in range(0b10000):
            press_arr = [
                (1 if i & j > 0 else 0)
                for j in (0b0001, 0b0010, 0b0100, 0b1000)
            ]
            if sum(press_arr) % 2 != presses % 2 or sum(press_arr) > presses:
                continue
            status = ["0"] * n
            for i, v in enumerate(press_arr):
                if not v:
                    continue
                button(i, status)
            status_set.add("".join(status))

        return len(status_set)


# @lc code=end
print(Solution().flipLights(3, 4))
