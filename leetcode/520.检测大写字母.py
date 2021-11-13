#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True

        first_letter, second_letter, left_letters = word[0], word[1], word[2:]
        first_state = ord('a') <= ord(first_letter) <= ord('z')
        second_state = ord('a') <= ord(second_letter) <= ord('z')

        if first_state and not second_state:
            return False

        letter_min = ord('a') if second_state else ord('A')
        letter_max = ord('z') if second_state else ord('Z')

        return all(
            letter_min <= ord(l) <= letter_max
            for l in left_letters
        )

# @lc code=end
