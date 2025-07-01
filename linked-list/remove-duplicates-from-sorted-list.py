# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 循环遍历链表，因为是已排序，所以如果下个结点值等于当前结点，就跳过
        # 否则就移动到下个结点
        if head is None:
            return None
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head