class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        # for i in range(2 * len(nums) - 1, -1, -1):
        #     while len(stack) > 0 and nums[stack[-1]] <= nums[i % len(nums)]:
        #         stack.pop()
        #     if len(stack) > 0:
        #         res[i % len(nums)] = nums[stack[-1]]
        #     stack.append(i % len(nums))
        for i in range(2 * len(nums) - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
            if len(stack) > 0:
                res[i % len(nums)] = stack[-1]
            stack.append(nums[i % len(nums)])
        return res


s = Solution()
print(s.nextGreaterElements([4, 7, 2, 3, 6]))
