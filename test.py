class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        from functools import cmp_to_key
        key = cmp_to_key(lambda x,y: int(y+x)-int(x+y))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'


s = Solution()
print(s.largestNumber([1, 3, 2, 4]))
