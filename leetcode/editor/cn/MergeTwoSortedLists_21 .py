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

        ret, one = l1 if l1.val < l2.val else l2
        anther = l2 if l1.val < l2.val else l2
        self.link(one, anther)

        return ret

    def link(self, one: ListNode, anther: ListNode):
        if one is None or anther is None:
            return

        if one.val < anther.val:
            if one.next is not None:
                one = one.next
                self.link(one, anther)
            else:
                one.next = anther
        else:
            if anther.next is not None:
                anther = anther.next
                self.link(one, anther)
            else:
                anther.next = one


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    l1 = [ListNode(1)]
    Solution().mergeTwoLists(l1, l2)
