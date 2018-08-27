class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        dp = []
        for i in range(len_s):
            dp.append([0] * len_s)
        for i in range(len_s):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    dp[i][j] = dp[i - 1][j + 1] + 2
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i - 1][j])

        return dp


s = Solution()
print(s.longestPalindromeSubseq('bawbaob'))
