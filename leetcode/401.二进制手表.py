#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        res = []

        def dfs(path, start):
            if start == 10 and bin(path).count('1') == turnedOn:
                hour = path >> 6
                minute = path & 0b0000111111
                if hour < 12 and minute < 60:
                    res.append('%s:%02d' % (hour, minute))
                return
            if start == 10:
                return
            dfs(path << 1, start + 1)
            dfs((path << 1) + 1, start + 1)

        dfs(0, 0)

        return res

# @lc code=end
