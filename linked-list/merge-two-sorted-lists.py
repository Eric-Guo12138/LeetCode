# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #新建一个list3用来存储结果
        #比较list1和list2的值，将较小的先加入list3
        list3 = cur = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return list3.next