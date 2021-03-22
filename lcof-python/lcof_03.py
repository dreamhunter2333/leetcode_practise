# -*- coding: utf-8 -*-
"""
    找出数组中重复的数字。

    在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

    示例 1：

    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3

    限制：

    2 <= n <= 100000
"""
from typing import List


class Solution:

    # 哈希表/数组标记
    def findRepeatNumber1(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)
        return -1

    # 排序
    def findRepeatNumber2(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1

    # 原地交换
    def findRepeatNumber3(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # 位置错误时进行交换
            while nums[i] != i:
                # 如果交换的目标位置和当前位置的值相等，即重复
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                # 交换位置，使 i 位置的元素正确
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


print(Solution().findRepeatNumber1([2, 3, 1, 0, 2, 5, 3]))
print(Solution().findRepeatNumber2([2, 3, 1, 0, 2, 5, 3]))
print(Solution().findRepeatNumber3([2, 3, 1, 0, 2, 5, 3]))
