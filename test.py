class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        times = []
        last = 0
        res = n * [0]
        for log in logs:
            tmp = log.split(':')
            if tmp[1] == 'start':
                stack.append([int(tmp[0]), int(tmp[2])])
                times.append(0)
            elif tmp[1] == 'end':
                dec_time = 0
                all_tmp_time = int(tmp[2]) - stack.pop()[1] + 1
                while times and times[-1] != 0:
                    dec_time += times.pop()
                res[int(tmp[0])] += all_tmp_time - dec_time
                times.pop()
                times.append(all_tmp_time)
            # print(stack, '-----', times, '====', res)
        return res


s = Solution()
print(s.exclusiveTime(2,["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))
