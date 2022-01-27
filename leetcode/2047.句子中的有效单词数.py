#
# @lc app=leetcode.cn id=2047 lang=python3
#
# [2047] 句子中的有效单词数
#

# @lc code=start

class Solution:
    def countValidWords(self, sentence: str) -> int:

        def is_valid(token: str) -> int:
            hasHyphens = False
            for i, ch in enumerate(token):
                if ch.isdigit() or (ch in "!.," and i < len(token) - 1):
                    return 0
                if ch == '-':
                    if hasHyphens or (
                        i == 0 or i == len(token) - 1
                    ) or (
                        not token[i - 1].islower() or not token[i + 1].islower()
                    ):
                        return 0
                    hasHyphens = True
            return 1

        return sum(is_valid(token) for token in sentence.split())


# print(Solution().countValidWords("cat and  dog"))
# @lc code=end
