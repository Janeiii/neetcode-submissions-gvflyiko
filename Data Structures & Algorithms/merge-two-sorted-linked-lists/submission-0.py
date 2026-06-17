# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pt1, pt2 = list1, list2
        dummy = ListNode(0)
        curr = dummy          # start at dummy

        while pt1 and pt2:    # only while both are non-null
            if pt1.val <= pt2.val:
                curr.next = pt1
                pt1 = pt1.next
            else:
                curr.next = pt2
                pt2 = pt2.next
            curr = curr.next

        curr.next = pt1 if pt1 else pt2

        return dummy.next