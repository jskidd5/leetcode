class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 1000000007
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 5
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, N + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] = dp[i] % mod
        return dp


s = Solution()
print(s.numTilings(5))
