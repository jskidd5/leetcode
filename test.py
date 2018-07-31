class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        s1 = [0] * len(prices)
        s2 = [0] * len(prices)
        s3 = [0] * len(prices)
        s1[0] = 0 - prices[0]
        for i in range(1, len(prices)):
            s1[i] = max(s1[i - 1], s3[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
            s3[i] = max(s3[i - 1], s2[i - 1])
        print(s1)
        print(s2)
        print(s3)
        return max(max(s2), max(s3))


s = Solution()
print(s.maxProfit([4, 2, 7, 1, 11]))
