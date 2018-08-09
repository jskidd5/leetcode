class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        len_p = len(pairs)
        if len_p <= 0:
            return 0
        pairs.sort()
        dp = [0] * len_p
        dp[0] = 1
        for i in range(1, len_p):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[j], dp[i])
            dp[i] += 1
        return dp


s = Solution()
print(s.findLongestChain([[-10, -8], [-6, -4], [-5, 0], [-4, 7], [1, 7], [6, 10], [8, 9], [9, 10]]))
