#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和
        result, num_sum = 0, 0
        sum_list = {0: 1}
        for num in nums:
            num_sum += num
            if num_sum - k in sum_list:
                result += sum_list[num_sum - k]
            sum_list[num_sum] = sum_list.get(num_sum, 0) + 1
        return result


print(Solution().subarraySum(nums=[1, 1, 1], k=2))
# @lc code=end
