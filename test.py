class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        len_s = len(s)
        dp = [0] * (len_s + 1)
        dp[0] = 1
        for i in range(1, len_s + 1):
            for w in wordDict:
                print(s[i - len(w):i])
                if len(w) <= i and w == s[i - len(w):i] and dp[i - len(w)] == 1:
                    dp[i] = 1
        if dp[-1] == 1:
            return True
        else:
            return False


s = Solution()
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
