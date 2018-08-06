from itertools import combinations


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        dp = [0] * len_s
        if len_s <= 0:
            return 0
        if s[0] == '0':
            return 0
        if len_s <= 1:
            return 1
        dp[0] = 1
        if s[1] != '0':
            dp[1] += 1
        if int(s[0:2]) <= 26:
            dp[1] += 1
        for i in range(2, len_s):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 1 <= int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                dp[i] += dp[i - 2]
            if dp[i] == 0:
                return 0
        return dp[-1]


s = Solution()
print(s.numDecodings('101'))
