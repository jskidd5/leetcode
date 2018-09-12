class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        dp = []
        for i in range(len_s1 + 1):
            dp.append([0] * (len_s2 + 1))
        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for i in range(1, len_s2 + 1):
            dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    tmp = 0
                else:
                    tmp = ord(s1[i - 1]) + ord(s2[j - 1])
                dp[i][j] = min(dp[i - 1][j - 1] + tmp, dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        return dp[-1][-1]


s = Solution()
print(s.minimumDeleteSum(
    "cicsddawqxrotwfehpfzxjukgumtcplecvgumpfitwowmtuhlgcbssisieoqgsfvavvaordkzwxpnppfjurckhyzeugkjowqzvojzigkrehiapcsiwwhvchrzhcsdgqyaovqzgbicnsstcofnmiipqxmjldknkcojlhzdprkqrqzbybexhmcfxhezzbwbfcbvnxrhatlklhadltciubrubudxthujdhtipicnvgangdpqicshcmmoacaonfsssjujzkznmxamgvlmaleovrcqijsdhnr",
    "zkhkcdscdrgpqjqtksxiztcmymfgttiqntizhfafbvmjbjurxtbtnwilunqfmkkuvtgjzeoiunmqqbqoppejtzafjpbickphuvvmuhzvuxmsoeezvtlgfxjjjuwieobwldmyrfamokmewopvnmoiymfevorwanmicfumifjmrrhreeqkvmqgmwdfcmhxpujcbyfwdwqkbzovzuxzntwksedzzkdnqjpxhsqmffiwtxjedlbcpgfnetafbdxibsbntvqahhtbmbtdcgiedwdjnfbeqnydooasjdvxcyqqojiretcgeeycjrqqlxtuujmvzqrsrazvifeszibswkreosvzaexridrrcwptjavetgiiockenusrwsufnvskeumjiyvmyyadsqdwectoamfvpvcsalqtnpettilatie"))
