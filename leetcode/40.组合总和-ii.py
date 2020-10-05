#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序
        candidates.sort()
        self.candidates = candidates
        self.result = []
        self.candidates_len = len(candidates)
        self.combine_sum_2(0, [], target)
        return self.result

    def combine_sum_2(self, start, path, cur_target):
        # cur_target 为 0 时结束
        if not cur_target:
            self.result.append(path)
            return

        for i in range(start, self.candidates_len):
            # 相同数字只取第一个
            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue
            # 超出范围提前结束
            if self.candidates[i] > cur_target:
                break
            # 符合条件继续递归
            self.combine_sum_2(i + 1, path + [self.candidates[i]], cur_target - self.candidates[i])


if __name__ == "__main__":
    print(Solution().combinationSum2(candidates=[10,1,2,7,6,1,5], target=8))

# @lc code=end

