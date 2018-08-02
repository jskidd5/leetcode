class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0:
            return []
        nums.sort()
        dp = [1] * len(nums)
        res = []
        for i in range(len(nums)):
            res.append([])
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        res[i].append(nums[j])
                    dp[i] = max(dp[j] + 1, dp[i])
            res[i].append(nums[i])
        return res


s = Solution()
print(s.largestDivisibleSubset([1, 2, 3, 4, 6, 24]))
