class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        len_s = len(S)
        len_t = len(T)
        s_i = len_s - 1
        s_cnt = 0
        t_i = len_t - 1
        t_cnt = 0
        while s_i >= 0 or t_i >= 0:
            while s_i >= 0 and (S[s_i] == '#' or s_cnt > 0):
                if S[s_i] == '#':
                    s_cnt += 1
                    s_i -= 1
                elif s_cnt > 0:
                    s_cnt -= 1
                    s_i -= 1
            tmp_s = ''
            if s_i >= 0:
                tmp_s = S[s_i]
                s_i -= 1
            while t_i >= 0 and (T[t_i] == '#' or t_cnt > 0):
                if T[t_i] == '#':
                    t_cnt += 1
                    t_i -= 1
                elif t_cnt > 0:
                    t_cnt -= 1
                    t_i -= 1
            tmp_t = ''
            if t_i >= 0:
                tmp_t = T[t_i]
                t_i -= 1
            if tmp_t != tmp_s:
                return False
        if s_i != t_i:
            return False
        return True


s = Solution()
print(s.backspaceCompare("s#v", "v"))
