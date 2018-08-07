class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_n = len(nums)
        if len_n <= 0:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i - n]
        return dp[-1]


s = Solution()
print(s.combinationSum4([], 0))
