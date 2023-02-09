#
# @lc app=leetcode.cn id=1797 lang=python3
#
# [1797] 设计一个验证系统
#

# @lc code=start
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.codeMap = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.codeMap[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        genTime = self.codeMap.get(tokenId)
        if not genTime or genTime + self.timeToLive <= currentTime:
            return
        self.codeMap[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.codeMap = {
            tokenId: genTime
            for tokenId, genTime in self.codeMap.items()
            if genTime + self.timeToLive > currentTime
        }
        return len(self.codeMap)


# @lc code=end
# Your AuthenticationManager object will be instantiated and called as such:
obj = AuthenticationManager(5)
obj.generate("aaa", 1)
obj.renew("aaa", 2)
print(obj.countUnexpiredTokens(6))
obj.generate("bbb", 7)
obj.renew("aaa", 8)
obj.renew("bbb", 10)
print(obj.countUnexpiredTokens(15))
