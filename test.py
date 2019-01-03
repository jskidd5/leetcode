class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        size = 0
        for s in S:
            if s.isdigit():
                size = size * int(s)
            else:
                size += 1
        for s in reversed(S):
            K = K % size
            if s.isalpha() and 0 == K:
                return s
            if s.isdigit():
                size = size / int(s)
            else:
                size -= 1
        return K


s = Solution()
print(s.decodeAtIndex("a2345678999999999999999",1))
