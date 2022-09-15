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

        for press_arr in (
            [i, j, k, p]
            for i in range(2)
            for j in range(2)
            for k in range(2)
            for p in range(2)
            if (
                i + j + k + p
            ) % 2 == presses % 2 and (
                i + j + k + p
            ) <= presses
        ):
            print(press_arr)
            status = ["0"] * n
            for i, v in enumerate(press_arr):
                if not v:
                    continue
                button(i, status)
            status_set.add("".join(status))

        return len(status_set)


# @lc code=end
print(Solution().flipLights(3, 2))
