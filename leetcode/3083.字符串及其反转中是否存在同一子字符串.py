#
# @lc app=leetcode.cn id=3083 lang=python3
#
# [3083] 字符串及其反转中是否存在同一子字符串
#

# @lc code=start
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        pre = s[0]
        cache = set()
        for char in s[1:]:
            cache.add(f"{char}{pre}")
            if f"{pre}{char}" in cache:
                return True
            pre = char
        return False


# @lc code=end
