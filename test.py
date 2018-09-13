class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        dp = []
        up = []
        down = []
        left = []
        right = []
        for i in range(N):
            dp.append([1] * N)
            up.append([0] * N)
            down.append([0] * N)
            left.append([0] * N)
            right.append([0] * N)
        for i in mines:
            dp[i[0]][i[1]] = 0
        for i in range(0, N):
            for j in range(0, N):
                if dp[i][j] == 1:
                    if i >= 1 and dp[i - 1][j] == 1:
                        up[i][j] = up[i - 1][j] + 1
                    else:
                        up[i][j] = 1
                if dp[N - i - 1][j] == 1:
                    if i > 0 and dp[N - i][j] == 1:
                        down[N - i - 1][j] = down[N - i][j] + 1
                    else:
                        down[N - i - 1][j] = 1
                if dp[i][j] == 1:
                    if j >= 1 and dp[i][j - 1] == 1:
                        left[i][j] = left[i][j - 1] + 1
                    else:
                        left[i][j] = 1
                if dp[i][N - j - 1] == 1:
                    if j > 0 and dp[i][N - j] == 1:
                        right[i][N - j - 1] = right[i][N - j] + 1
                    else:
                        right[i][N - j - 1] = 1
        res = []
        for i in range(0, N):
            for j in range(0, N):
                if dp[i][j] == 1:
                    dp[i][j] = min(up[i][j], down[i][j], left[i][j], right[i][j])
            res.append(max(dp[i]))
        return max(res)


s = Solution()
print(s.orderOfLargestPlusSign(1, [[0, 0]]))
