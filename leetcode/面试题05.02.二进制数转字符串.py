#
# 面试题 05.02. 二进制数转字符串
#


class Solution:
    def printBin(self, num: float) -> str:
        res = "0."
        count = 30
        while count >= 0 and num > 0:
            num = num * 2
            res += f"{int(num)}"
            num = num % 1
            count -= 1
        return res if count >= 0 else "ERROR"


print(Solution().printBin(0.625))
print(Solution().printBin(0.1))
