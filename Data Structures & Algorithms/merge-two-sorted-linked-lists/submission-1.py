# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = ListNode(0)
        head = merged

        while list1 or list2:
            if list1 and list2 and list1.val == list2.val:

                temp1 = ListNode(list1.val)
                merged.next = temp1
                merged = merged.next
                temp2 = ListNode(list2.val)
                merged.next = temp2
                merged = merged.next

                list1 = list1.next
                list2 = list2.next

            elif list1 and list2 and list1.val < list2.val:
                temp1 = ListNode(list1.val)
                merged.next = temp1
                merged = merged.next 
                list1 = list1.next
            elif list1 and list2 and list1.val > list2.val:
                temp1 = ListNode(list2.val)
                merged.next = temp1
                merged = merged.next 
                list2 = list2.next
            else:
                if list1:
                    while list1:
                        temp = ListNode(list1.val)
                        merged.next = temp
                        merged = merged.next
                        list1 = list1.next
                if list2:
                    while list2:
                        temp = ListNode(list2.val)
                        merged.next = temp
                        merged = merged.next
                        list2 = list2.next

        return head.next