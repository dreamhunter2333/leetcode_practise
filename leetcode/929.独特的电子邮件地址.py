#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#
from typing import List


# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cache = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.replace(".", "")
            if "+" in name:
                name = name[:name.index("+")]
            cache.add("@".join([name, domain]))
        return len(cache)


# @lc code=end
print(Solution().numUniqueEmails([
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]))
print(Solution().numUniqueEmails([
    "a@leetcode.com",
    "b@leetcode.com",
    "c@leetcode.com"
]))
