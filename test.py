class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        len_a = len(A)
        sum_a = [0] * (len_a + 1)
        for i in range(1, len_a + 1):
            sum_a[i] = sum_a[i - 1] + A[i - 1]
        dp = []
        for i in range(len_a + 1):
            dp.append([0.0] * (K + 1))
        for i in range(1, len_a + 1):
            k = 1
            dp[i][k] = sum_a[i] / i
            k += 1
            while k <= i and k <= K:
                for j in range(1, i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + ((sum_a[i] - sum_a[j]) / (i - j)))
                k += 1
        return dp[-1][-1]


s = Solution()
print(s.largestSumOfAverages([4, 1, 7, 5, 6, 2, 3], 4))
