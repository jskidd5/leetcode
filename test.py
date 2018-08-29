class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        dp = [1] * len_s
        res = 0
        for i in range(len_s):
            res += 1
            cnt = 1
            while i - cnt + 1 >= 0 and i + cnt < len_s:
                if s[i - cnt + 1] == s[i + cnt]:
                    res += 1
                else:
                    break
                cnt += 1
            cnt = 1
            while i - cnt >= 0 and i + cnt < len_s:
                if s[i - cnt] == s[i + cnt]:
                    res += 1
                else:
                    break
                cnt += 1
        return res


s = Solution()
print(s.countSubstrings('aaa'))
