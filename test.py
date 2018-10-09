# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        head = root
        len_r = 0
        while head:
            head = head.next
            len_r += 1
        index = 0
        cnt = 0
        pre_cnt = len_r // k
        mod_cnt = len_r % k
        head = root
        tmp_head = ListNode(-1)
        tmp_node = tmp_head
        while head:
            if cnt < pre_cnt:
                tmp_node.next = ListNode(head.val)
                head = head.next
                tmp_node = tmp_node.next
                cnt += 1
            elif mod_cnt > 0:
                mod_cnt -= 1
                tmp_node.next = ListNode(head.val)
                head = head.next
                res.append(tmp_head.next)
                index += 1
                tmp_head.next = None
                tmp_node = tmp_head
                cnt = 0
            else:
                res.append(tmp_head.next)
                index += 1
                tmp_head.next = None
                tmp_node = tmp_head
                cnt = 0
        if tmp_head.next:
            res.append(tmp_head.next)
            index += 1
        while index < k:
            res.append(None)
            index += 1
        return res


v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v2 = [5, 6, 4]
n1 = ListNode(-1)
n2 = ListNode(-1)
t1 = n1
t2 = n2
for i in v1:
    t1.next = ListNode(i)
    t1 = t1.next
for i in v2:
    t2.next = ListNode(i)
    t2 = t2.next
n = n1
while n:
    #print(n.val)
    n = n.next
n = n2
while n:
    #print(n.val)
    n = n.next
s = Solution()
n = s.splitListToParts(n1.next, 12)
print()
for i in n:
    while i:
        print(i.val)
        i = i.next
    print()
