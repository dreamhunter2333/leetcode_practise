#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        n = len(res)

        for i in range(n):
            if res[i] != "?":
                continue
            for b in ascii_lowercase:
                if not (
                    i > 0 and res[i - 1] == b or
                    i < n - 1 and res[i + 1] == b
                ):
                    res[i] = b
                    break

        return "".join(res)


# print(Solution().modifyString("??yw?ipkj?"))
# @lc code=end
