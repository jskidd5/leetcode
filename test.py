class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int   1000000007
        """
        # len_a = len(A)
        # right_array = [1] * len_a
        # left_array = [1] * len_a
        # res = 0
        # mod = 10 ** 9 + 7
        # stack = []
        # for i in range(len_a):
        #     for j in range(i - 1, -1, -1):
        #         if A[i] < A[j]:
        #             left_array[i] += 1
        #         else:
        #             break
        #     for j in range(i + 1, len_a):
        #         if A[i] <= A[j]:
        #             right_array[i] += 1
        #         else:
        #             break
        # for i in range(len_a):
        #     res += (right_array[i] * left_array[i]) * A[i]
        # return res % mod
        ans = 0
        maxindex = len(A) - 1
        left = []
        right = []
        for i in range(0, maxindex + 1):
            numleft = 1
            while i - numleft >= 0 and A[i - numleft] > A[i]:
                numleft += left[i - numleft]
            left.append(numleft)
            print(left)
            numright = 1
            while maxindex - i + numright <= maxindex and A[maxindex - i + numright] >= A[maxindex - i]:
                numright += right[i - numright]
            right.append(numright)
            print(right)
            print()
        for i in range(0, maxindex + 1):
            ans += left[i] * right[maxindex - i] * A[i]
        return ans % 1000000007


s = Solution()
print(s.sumSubarrayMins([3, 4, 5, 1]))
