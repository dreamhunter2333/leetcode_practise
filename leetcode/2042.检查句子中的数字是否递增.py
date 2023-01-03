#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pre = -1
        for lett in s.split(" "):
            if not lett.isdigit():
                continue
            num = int(lett)
            if num <= pre:
                return False
            pre = num
        return True


# @lc code=end
print(Solution().areNumbersAscending("4 5 11 26"))
