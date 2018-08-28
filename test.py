class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        len_p = len(p)
        dp = [0] * 26
        dp[ord(p[len_p - 1]) - 97] = 1
        cnt = 1
        for i in range(len_p - 2, -1, -1):
            if ord(p[i + 1]) - ord(p[i]) == 1 or ord(p[i + 1]) - ord(p[i]) == -25:
                cnt += 1
            else:
                cnt = 1
            dp[ord(p[i]) - 97] = max(cnt, dp[ord(p[i]) - 97])
        return sum(dp)


s = Solution()
print(s.findSubstringInWraproundString('zab'))
