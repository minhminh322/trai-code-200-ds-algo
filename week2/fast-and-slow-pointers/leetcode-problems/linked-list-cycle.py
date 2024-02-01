# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # First Approach using Set
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next

        # return False

        # Second Approach using Fast&Slow pointers
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
