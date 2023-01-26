# 面试题45 把数组排成最小的数
from typing import List
from functools import cmp_to_key


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return "".join(
            f"{num}"
            for num in sorted(nums, key=cmp_to_key(self.compare))
        )

    def compare(self, num1: int, num2: int):
        return 1 if f"{num1}{num2}" >= f"{num2}{num1}" else -1


print(Solution().minNumber([3, 30, 34, 5, 9]))
