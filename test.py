# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        res = ListNode(-1)
        res.next = head
        pre = head
        curr = head.next
        while curr:
            tmp = curr.next
            curr.next = res.next
            res.next = curr
            pre.next = tmp
            n = res
            while n:
                print(n.val)
                n = n.next
            curr = tmp
            print()
        return res.next


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
    # print(n.val)
    n = n.next
n = n2
while n:
    # print(n.val)
    n = n.next
s = Solution()
n = s.numComponents(n1.next, [0, 3, 1,2])
print()
while n:
    print(n.val)
    n = n.next
