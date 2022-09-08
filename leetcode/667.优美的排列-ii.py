#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#
from typing import List


# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            answer.append(i)
            if i != j:
                answer.append(j)
            i, j = i + 1, j - 1
        return answer

# @lc code=end
