class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        map_n = {}
        for i in range(len_n):
            if nums[i] in map_n:
                map_n[nums[i]] += 1
            else:
                map_n[nums[i]] = 1
        dp = [0] * 10001
        dp[1] = map_n.get(1, 0)
        for i in range(2, 10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * map_n.get(i, 0))
        return dp[-1]


s = Solution()
print(s.deleteAndEarn([1]))
