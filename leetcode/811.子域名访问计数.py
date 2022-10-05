#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            while domain:
                count_map[domain] += int(count)
                domain = domain.split(
                    ".", maxsplit=1
                )[1] if "." in domain else None
        return [
            f"{count} {domain}"
            for domain, count in count_map.items()
        ]


# @lc code=end
print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))
print(Solution().subdomainVisits([
    "900 google.mail.com",
    "50 yahoo.com", "1 intel.mail.com",
    "5 wiki.org"
]))
