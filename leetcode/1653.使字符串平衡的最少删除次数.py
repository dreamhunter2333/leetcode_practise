#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        right_a = s.count('a')
        left_b = 0
        res = right_a
        for i in s:
            if i == 'a':
                right_a -= 1
            else:
                left_b += 1
            res = min(res, left_b + right_a)

        return res


# @lc code=end
print(Solution().minimumDeletions("aababbab"))
print(Solution().minimumDeletions("bbaaaaabb"))
