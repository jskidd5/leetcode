class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        dp = [1]
        res = [s[0]]
        for i in range(1, len(s)):
            dp.append(1)
            res.append(s[i])
            left = i - 1
            right = i + 1
            if left >= 0 and s[i] == s[left]:
                dp[i] += 1
                res[i] = s[left] + res[i]
                left -= 1
            elif right < len(s) and s[i] == s[right]:
                dp[i] += 1
                res[i] = res[i] + s[right]
                right += 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    dp[i] += 2
                    res[i] = s[left] + res[i] + s[right]
                else:
                    break
                left -= 1
                right += 1
        r1 = res[dp.index(max(dp))]
        dp = [1]
        res = [s[0]]
        for i in range(1, len(s)):
            dp.append(1)
            res.append(s[i])
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    dp[i] += 2
                    res[i] = s[left] + res[i] + s[right]
                else:
                    break
                left -= 1
                right += 1
        r2 = res[dp.index(max(dp))]
        if len(r1) > len(r2):
            return r1
        else:
            return r2


s = Solution()
print(s.longestPalindrome('aaaa'))
