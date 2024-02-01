# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traversing the list with slow pointer,
        # make the fast pointer that traverse twice as fast
        # when fast pointer reaches the end of list, 
        # slow pointer must be in the middle
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow