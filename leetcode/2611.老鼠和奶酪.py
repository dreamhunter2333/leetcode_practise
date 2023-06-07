#
# @lc app=leetcode.cn id=2611 lang=python3
#
# [2611] 老鼠和奶酪
#
from typing import List


# @lc code=start
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        mouse1 = set(sorted(
            range(n),
            key=lambda i: (reward1[i] - reward2[i]), reverse=True
        )[:k])
        return sum(
            reward1[j] if j in mouse1 else reward2[j]
            for j in range(n)
        )


# @lc code=end
print(Solution().miceAndCheese(
    reward1=[1, 1, 3, 4], reward2=[4, 4, 1, 1], k=2
))
print(Solution().miceAndCheese(
    reward1=[1, 1], reward2=[1, 1], k=2
))
