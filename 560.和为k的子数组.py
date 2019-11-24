#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (42.15%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 25K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 
# 
# 说明 :
# 
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, num_sum = 0, 0
        sum_list = {0: 1}
        for num in nums:
            num_sum += num
            if num_sum - k in sum_list.keys():
                result += sum_list[num_sum - k]
            sum_list[num_sum] = sum_list.get(num_sum, 0) + 1
        return result
# @lc code=end

