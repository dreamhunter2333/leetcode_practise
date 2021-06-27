#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        cache1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        cache2 = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        res = 0
        temp = 0
        pre = None
        for i in range(len(s)):
            if pre in (None, s[i]):
                temp += cache1[s[i]]
                pre = s[i]
            elif pre in cache2 and s[i] in cache2[pre]:
                res -= 2 * temp
                temp = 0
                pre = None
            else:
                temp = cache1[s[i]]
                pre = s[i]
            res += cache1[s[i]]

        return res


print(Solution().romanToInt('III'))
# @lc code=end
