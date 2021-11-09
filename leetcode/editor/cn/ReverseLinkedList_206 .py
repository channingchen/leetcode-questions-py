# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2]
# 输出：[2,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围是 [0, 5000] 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
# 
#  进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？ 
#  
#  
#  Related Topics 递归 链表 
#  👍 2072 👎 0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        sub = self.reverseList(head.next)
        tail = sub
        while tail.next is not None:
            tail = tail.next

        tail.next = head
        head.next = None
        return sub


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        c = head
        c2 = head
        l = []
        while c is not None:
            l.append(c.val)
            c = c.next
        for i in reversed(l):
            c2.val = l[i]
            c2 = c2.next

        return head


# leetcode submit region end(Prohibit modification and deletion)

def link(l: list) -> ListNode:
    for i in range(len(l) - 1):
        l[i].next = l[i + 1]
    return l[0]


def printlist(n: ListNode):
    while n is not None:
        print(n.val, end=",")
        n = n.next
    print("")


if __name__ == '__main__':
    l = link([ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ])
    printlist(l)
    ret = Solution().reverseList(l)
    printlist(ret)
