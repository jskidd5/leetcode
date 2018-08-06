class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        len_row = len(matrix)
        if len_row <= 0:
            return 0
        len_col = len(matrix[0])
        dp = []
        for i in range(len_row):
            dp.append([0] * len_col)
        for i in range(len_col):
            if matrix[0][i] == '1':
                dp[0][i] = 1
        for i in range(len_row):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        for i in range(1, len_row):
            for j in range(1, len_col):
                if dp[i - 1][j] > 0 and dp[i][j - 1] > 0 and dp[i - 1][j - 1] > 0 and int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = int(matrix[i][j])
        res = []
        for i in dp:
            res.append(max(i))
        l = max(res)
        return dp


s = Solution()
print(s.maximalSquare(
    [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]))
