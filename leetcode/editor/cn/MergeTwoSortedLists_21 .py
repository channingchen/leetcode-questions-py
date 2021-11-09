# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个链表的节点数目范围是 [0, 50] 
#  -100 <= Node.val <= 100 
#  l1 和 l2 均按 非递减顺序 排列 
#  
#  Related Topics 递归 链表 👍 2012 👎 0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        ret = l1 if l1.val < l2.val else l2
        c1 = ret
        c2 = l2 if l1 == ret else l1
        self.link(c1, c2)

        return ret

    def link(self, c1: ListNode, c2: ListNode):
        if c1 is None or c2 is None:
            return

        while c1.next is not None and c1.next.val < c2.val:
            c1 = c1.next

        temp = c1.next
        c1.next = c2
        c2 = temp

        self.link(c1.next, c2)


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
    l1 = link([ListNode(1), ListNode(2), ListNode(4)])
    l2 = link([ListNode(1), ListNode(3), ListNode(4)])

    printlist(l1)
    printlist(l2)
    ret = Solution().mergeTwoLists(l1, l2)
    printlist(ret)
