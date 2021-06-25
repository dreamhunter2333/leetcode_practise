#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead = set(deadends)
        cache1 = {}
        cache2 = {}

        def run(cur, flag):
            cur += flag
            if cur == 10 and flag == 1:
                return 0
            if cur == -1 and flag == -1:
                return 9
            return cur

        def bfs(nums1, nums2, count1, count2):
            if not nums1 or not nums2:
                return -1
            next_nums = set()
            num_flag = len(nums1) < len(nums2)
            nums = nums1 if num_flag else nums2
            cache, other_cache = (cache1, cache2) if num_flag else (cache2, cache1)
            count = count1 if num_flag else count2
            for cur_str in nums:
                print(cur_str)
                if cur_str in dead or cur_str in cache:
                    continue
                cache[cur_str] = count
                if cur_str in other_cache:
                    return count + other_cache[cur_str]

                a, b, c, d = list(map(int, cur_str))

                for i in range(8):
                    flag = 1 if i % 2 else -1
                    index = i // 2
                    next_num = [a, b, c, d]
                    next_num[index] = run(next_num[index], flag)
                    next_nums.add(''.join(map(str, next_num)))
            args = [
                next_nums, nums2, count1+1, count2
            ] if num_flag else [
                nums1, next_nums, count1, count2+1
            ]
            return bfs(*args)

        return bfs({target}, {"0000"}, 0, 0)


print(Solution().openLock(
    ["0201", "0101", "0102", "1212", "2002"],
    "0202"
))
# @lc code=end
