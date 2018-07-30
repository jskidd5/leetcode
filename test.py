class Solution:
    def lengthOfLIS(self, nums):
        res = []
        if len(nums) <= 0:
            return 0
        for i, n in enumerate(nums):
            tmp = [1]
            for j in range(i):
                cnt = 1
                if n > nums[i - j - 1]:
                    tmp.append(cnt + res[i - j - 1])
            res.append(max(tmp))
        return max(res)


# class Solution:
#     def lengthOfLIS(self, nums):
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1
#         track = [1] * len(nums)
#
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     if track[j] + 1 > track[i]:
#                         track[i] = track[j] + 1
#
#     return max(track)


import time

s = Solution()
start = time.clock()

s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])

end = time.clock()
print(end - start)
