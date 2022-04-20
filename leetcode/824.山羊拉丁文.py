#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#
# @lc code=start
META_LETTER = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


class Solution:

    def toGoatLatin(self, sentence: str) -> str:
        return " ".join(
            (
                word
                if word[0] in META_LETTER else
                (word[1:] + word[0])
            ) + "ma" + "a" * i
            for i, word in enumerate(sentence.split(" "), 1)
        )


# print(Solution().toGoatLatin("I speak Goat Latin"))
# print(Solution().toGoatLatin("The quick brown fox jumped over the lazy dog"))
# @lc code=end
