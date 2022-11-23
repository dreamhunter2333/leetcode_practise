#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count_map = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            target = 0
            while i:
                target += i % 10
                i = i // 10
            count_map[target] += 1
        return max(count_map.values())


# @lc code=end
print(Solution().countBalls(lowLimit=1, highLimit=10))
print(Solution().countBalls(lowLimit=5, highLimit=15))
print(Solution().countBalls(lowLimit=19, highLimit=28))
