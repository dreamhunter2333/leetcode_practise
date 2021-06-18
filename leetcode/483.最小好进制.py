#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        def check(x, m):
            ans = 0
            for _ in range(m):
                if ans > (num - 1) / x:
                    return 1
                ans = ans*x + 1
            if ans == num:
                return 0
            elif ans < num:
                return -1
            elif ans > num:
                return 1
        for i in range(64, 0, -1):
            l = 2
            r = num
            while l < r:
                mid = l + (r - l)//2
                tmp = check(mid, i)
                if tmp == 0:
                    return str(mid)
                elif tmp < 0:
                    l = mid + 1
                elif tmp > 0:
                    r = mid
        return str(ans)

# @lc code=end
