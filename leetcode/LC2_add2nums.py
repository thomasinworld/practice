# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []
        current = l1
        while current:
            num1 = [current.val] + num1
            current = current.next

        current = l2
        while current:
            num2 = [current.val] + num2
            current = current.next
        
        num = int(''.join(map(str, num1))) + int(''.join(map(str, num2)))

        dummy = ListNode(0)
        curr = dummy
        
        for digit in reversed(str(num)):
            curr.next = ListNode(int(digit))
            curr = curr.next
        
        return dummy.next
