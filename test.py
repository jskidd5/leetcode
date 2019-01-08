class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        cnt = 1
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            cnt += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, cnt])
        print(self.stack)
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
l = ["next", "next", "next", "next", "next", "next", "next"]
v = [[], [100], [80], [60], [70], [60], [75], [85]]
obj = StockSpanner()
cnt = 1
for i in l:
    param_1 = getattr(obj, i)(v[cnt][0])
    cnt += 1
    print(param_1)

# s = Solution()
# print(s.decodeAtIndex("a2345678999999999999999",1))
