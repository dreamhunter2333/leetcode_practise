#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = k - 1
        n = len(blocks)
        count_w = sum(
            1 for p in range(k)
            if blocks[p] == "W"
        )
        res = count_w
        while j < n - 1:
            if blocks[i] == "W":
                count_w -= 1
            if blocks[j+1] == "W":
                count_w += 1
            res = min(res, count_w)
            i += 1
            j += 1

        return res


# @lc code=end
print(Solution().minimumRecolors(blocks="WBBWWBBWBW", k=7))
print(Solution().minimumRecolors(blocks="WBWBBBW", k=2))
print(Solution().minimumRecolors(blocks="WBWW", k=2))
