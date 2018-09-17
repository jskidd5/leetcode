class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len_n = len(A)
        if len_n <= 0:
            return 0
        dp1 = [0] * len_n
        dp2 = [0] * len_n
        for i in range(len_n):
            dp1[i] = i
            dp2[i] = i + 1
        for i in range(1, len_n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp1[i] = dp1[i - 1]
                dp2[i] = dp2[i - 1] + 1
            if B[i] > A[i - 1] and A[i] > B[i - 1]:
                dp1[i] = min(dp1[i], dp2[i - 1])
                dp2[i] = dp1[i - 1] + 1
        return min(dp1[-1], dp2[-1])


s = Solution()
print(s.minSwap([0, 4, 4, 5, 9], [0, 1, 6, 8, 10]))
