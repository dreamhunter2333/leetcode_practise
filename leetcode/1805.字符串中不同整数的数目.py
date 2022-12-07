#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        pre = ""
        res = set()
        for lett in (word + "a"):
            if lett.isdigit():
                pre += lett
            elif pre:
                res.add(int(pre))
                pre = ""
            else:
                pre = ""
        return len(res)


# @lc code=end
print(Solution().numDifferentIntegers("a123bc34d8ef34"))
