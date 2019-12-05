# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cursor1 = l1
        cursor2 = l2
        result = ListNode(0)
        cursor3 = result
        print(l1)
        print(result)
        while (cursor1 and cursor2):
            if cursor1.val < cursor2.val:
                cursor3.next = ListNode(cursor1.val)
                cursor1 = cursor1.next
            else:
                cursor3.next = ListNode(cursor2.val)
                cursor2 = cursor2.next
            cursor3 = cursor3.next
        
        while(cursor1):
            cursor3.next = ListNode(cursor1.val)
            cursor1 = cursor1.next
            cursor3 = cursor3.next
        
        while(cursor2):
            cursor3.next = ListNode(cursor2.val)
            cursor2 = cursor2.next
            cursor3 = cursor3.next
            
        return result.next