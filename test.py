class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 2:
            return False
        two = min(nums) - 1
        stack = []
        for i in range(n - 1, -1, -1):
            if nums[i] < two:
                return True
            while len(stack) > 0 and nums[i] > stack[-1]:
                two = stack[-1]
                stack.pop()
                print(stack)
            if len(stack) == 0 or stack[-1] > nums[i]:
                stack.append(nums[i])
            print(stack, two)
        return False


s = Solution()
print(s.find132pattern([4, 7, 2, 3, 6]))
