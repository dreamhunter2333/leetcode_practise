#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#

# @lc code=start
class Codec:

    def __init__(self) -> None:
        self.data = {}
        self.max_id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.max_id += 1
        self.data[self.max_id] = longUrl
        return f"http://tinyurl.com/{self.max_id}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        data_id = shortUrl.split("/")[-1]
        return self.data.get(int(data_id), "")


# @lc code=end
# Your Codec object will be instantiated and called as such:
codec = Codec()
assert "https://leetcode.com/problems/design-tinyurl" == codec.decode(
    codec.encode("https://leetcode.com/problems/design-tinyurl")
)
