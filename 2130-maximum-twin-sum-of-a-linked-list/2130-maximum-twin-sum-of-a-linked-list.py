# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        i=0
        j=len(arr)-1
        maxi=0
        while i<j:
            sumi=arr[i]+arr[j]
            maxi=max(maxi,sumi)
            i+=1
            j-=1
        return maxi
