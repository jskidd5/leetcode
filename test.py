class Solution:

    def maxProduct(self, nums):
        if nums == []:
            return 0
        min_res = 1
        max_res = 1
        res = [1] * len(nums)
        for i, n in enumerate(nums):
            if n == 0:
                min_res = 1
                max_res = 1
                res[i] = 0
            else:
                tmp = [n * max_res, n * min_res, n]
                max_res = max(tmp)
                min_res = min(tmp)
                res[i] = max_res
        return max(res)


s = Solution()
print(s.maxProduct([-3, -4, -5]))
