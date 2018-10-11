class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        flg = False
        res = []
        for i in nums1:
            index = list.index(nums2, i) + 1
            while index < len(nums2):
                if i < nums2[index]:
                    flg = True
                    break
                index += 1
            if flg:
                res.append(nums2[index])
            else:
                res.append(-1)
            flg = False
        return res

s = Solution()
print(s.nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))
