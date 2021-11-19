# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  返回同样按升序排列的结果链表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围 [0, 300] 内 
#  -100 <= Node.val <= 100 
#  题目数据保证链表已经按升序排列 
#  
#  Related Topics 链表 双指针 
#  👍 746 👎 0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        # 处理head
        cur = head
        cur = cur.next
        while cur:
            repeat = False
            while cur and cur.val == head.val:
                repeat = True
                cur = cur.next
            if repeat:
                head = cur
            else:
                break
            cur = cur.next if cur else cur

        if head is None:
            return head

        # 处理剩余重复部分
        last = head
        cur = head.next
        while last and cur:
            v = cur.val
            repeat = False
            while cur.next and cur.next.val == v:
                repeat = True
                cur = cur.next
                last.next = cur.next
            if not repeat:
                last = last.next
            cur = last.next if last.next else None

        return head


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                v = cur.next.val
                while cur.next and cur.next.val == v:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7]
    l = list(map(lambda x: ListNode(x), arr))
    for i in range(1, len(arr)):
        l[i - 1].next = l[i]

    r = Solution().deleteDuplicates(l[0])
    while r:
        print(r.val, end=",")
        r = r.next
