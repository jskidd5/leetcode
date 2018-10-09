# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        len_l1 = 0
        len_l2 = 0
        t1 = l1
        t2 = l2
        while t1:
            t1 = t1.next
            len_l1 += 1
        while t2:
            t2 = t2.next
            len_l2 += 1
        tmp = res
        if len_l1 > len_l2:
            tmp.next = l1
            tmp = tmp.next
            cnt = len_l1 - len_l2
            while cnt > 0:
                tmp = tmp.next
                cnt -= 1
            while l2:
                tmp.val += l2.val
                tmp = tmp.next
                l2 = l2.next
        else:
            tmp.next = l2
            tmp = tmp.next
            cnt = len_l2 - len_l1
            while cnt > 0:
                tmp = tmp.next
                cnt -= 1
            while l1:
                tmp.val += l1.val
                tmp = tmp.next
                l1 = l1.next

        pre = res
        curr = res.next
        while curr:
            if curr.val >= 10:
                if pre.val == -1:
                    tmp = pre.next
                    pre.next = ListNode(1)
                    pre.next.next = tmp
                else:
                    pre.val += 1
                curr.val -= 10
                pre = res
                curr = res.next
                continue
            pre = pre.next
            curr = curr.next
        return res.next


v1 = [9, 4, 4, 3]
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
    print(n.val)
    n = n.next
n = n2
while n:
    print(n.val)
    n = n.next
s = Solution()
n = s.addTwoNumbers(n1.next, n2.next)
print()
while n:
    print(n.val)
    n = n.next
