# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        ptr = result

        carry = 0

        while l1 is not None or l2 is not None or carry !=0:
            sum=0+carry
            if l1 is not None:
                sum+=l1.val
                l1=l1.next
            if l2 is not None:
                sum+=l2.val
                l2=l2.next
            
            carry = sum//10
            sum = sum%10
            ptr.next = ListNode(sum)
            ptr = ptr.next
        
        if carry == 1: ptr.next = ListNode(0)

        return result.next