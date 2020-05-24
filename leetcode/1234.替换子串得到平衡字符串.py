#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#
# https://leetcode-cn.com/problems/replace-the-substring-for-balanced-string/description/
#
# algorithms
# Medium (26.08%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 8.9K
# Testcase Example:  '"QWER"'
#
# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
# 
# 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
# 
# 
# 
# 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
# 
# 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
# 
# 请返回待替换子串的最小可能长度。
# 
# 如果原字符串自身就是一个平衡字符串，则返回 0。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "QWER"
# 输出：0
# 解释：s 已经是平衡的了。
# 
# 示例 2：
# 
# 输入：s = "QQWE"
# 输出：1
# 解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
# 
# 
# 示例 3：
# 
# 输入：s = "QQQW"
# 输出：2
# 解释：我们可以把前面的 "QQ" 替换成 "ER"。 
# 
# 
# 示例 4：
# 
# 输入：s = "QQQQ"
# 输出：3
# 解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s.length 是 4 的倍数
# s 中只含有 'Q', 'W', 'E', 'R' 四种字符
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def balancedString(self, s: str) -> int:

        ans = len(s)
        len_char = ans // 4

        extra = Counter(s) - Counter({c: len_char for c in 'QWER'})

        if not extra:
            return 0

        indices = defaultdict(list)
        extra_items = extra.items()
        continue_flag = True

        for i, c in enumerate(s):
    
            indices[c].append(i)
    
            if continue_flag and any(len(indices[k]) < extra[k] for k in 'QWER'):
                continue

            continue_flag = False

            # 计算 替换子串的最小可能长度
            ans = min(ans, i - min(indices[k][-v] for k, v in extra_items) + 1)

        return ans


if __name__ == "__main__":
    print(Solution().balancedString("WQWRQQQW"))

# @lc code=end

