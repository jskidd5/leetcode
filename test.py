class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res_cnt = 0
        len_n = len(nums)
        if len_n == 0:
            return 0
        dp = [1] * len_n
        res = [1] * len_n
        for i in range(1, len_n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        res[i] = res[j]
                    elif dp[j] + 1 == dp[i]:
                        res[i] += res[j]
                    dp[i] = max(dp[j] + 1, dp[i])
        max_cnt = max(dp)
        for i in range(len_n):
            if dp[i] == max_cnt:
                res_cnt += res[i]
        return dp, res, res_cnt


s = Solution()
print(s.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
