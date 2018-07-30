class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        res1 = [0] * len(nums)
        for i, n in enumerate(nums[1:]):
            res1[i] = max(res1[i - 2] + n, res1[i - 1])
        res2 = [0] * len(nums)
        for i, n in enumerate(nums[:-1]):
            res2[i] = max(res2[i - 2] + n, res2[i - 1])
        return max(max(res1), max(res2))


s = Solution()
print(s.rob([1, 2, 3]))
