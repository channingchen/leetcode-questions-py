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


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        # 处理head
        cur = head
        while cur:
            repeat = False
            while cur and cur.val == head.val:
                repeat = True
                cur = cur.next
            if repeat:
                head = cur
            cur = cur.next

        last = head
        while last and cur:
            repeat = False
            while cur and cur.val == last.val:
                repeat = True
                cur = cur.next
            if repeat:
                last = cur
            else:
                cur = cur.next if cur else cur

        return head

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    arr = [1, 1, 2, 3, 3, 4, 4, 5]
    l = list(map(lambda x: ListNode(x), arr))
    for i in range(1, len(arr)):
        l[i - 1].next = l[i]

    r = Solution().deleteDuplicates(l[0])
    while r:
        print(r.val, end=",")
        r = r.next
