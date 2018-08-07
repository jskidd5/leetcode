class Solution:
    def canPartition(self, nums):
        s=sum(nums)
        if s%2!=0:
            return False
        else:
            s=s//2
        dp=[False for x in range(s+1)]
        dp[0]=True
        for n in nums:
            for i in range(s, n-1, -1):
                if dp[i - n]:
                    dp[i] = True
            print(dp)
        return dp

s = Solution()
print(s.canPartition([1, 5, 11, 5]))
