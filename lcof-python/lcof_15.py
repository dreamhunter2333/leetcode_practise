"""
剑指 Offer 15. 二进制中1的个数
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n & 0xffffffff).count('1')
