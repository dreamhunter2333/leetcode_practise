#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#
from typing import Dict, Set


# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        nums = set(range(1, maxChoosableInteger + 1))
        if sum(nums) < desiredTotal:
            return False

        cache: Dict[Set[int], bool] = {}

        def dfs(nums: Set[int], cur_sum: int) -> bool:
            frozen_nums = frozenset(nums)
            if frozen_nums in cache:
                return cache[frozen_nums]
            for num in frozen_nums:
                if cur_sum + num >= desiredTotal:
                    cache[frozen_nums] = True
                    return True
                nums.remove(num)
                res = dfs(nums, cur_sum + num)
                nums.add(num)
                if not res:
                    cache[frozen_nums] = True
                    return True
            cache[frozen_nums] = False
            return False

        return dfs(nums, 0)


# @lc code=end
print(Solution().canIWin(10, 11))
print(Solution().canIWin(10, 0))
print(Solution().canIWin(10, 1))
