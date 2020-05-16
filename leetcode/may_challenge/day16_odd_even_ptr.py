'''
simple
'''
class Solution:
    def oddEvenList(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next




'''
fastest 24 ms
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
            
        i = 0
        cur = head
        while i < len(values):
            cur.val = values[i]
            cur = cur.next
            i+=2
        i = 1
        while i < len(values):
            cur.val = values[i]
            cur = cur.next
            i+=2
        return head


'''
fast 28 ms
to make i/p:  head of    1 ->  2 -> 3 -> 4 -> 5 -> null
to o/p: 1 -> 3 -> 5 -> 2 -> 4  -> null
	
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = ListNode(0)
        evens = ListNode(0)
        
        oddHead = odds
        evenHead = evens
        
        length = 1
        
        while head:
            if length % 2 == 0:
                evens.next = head
                evens = evens.next
            else:
                odds.next = head
                odds = odds.next
            
            length += 1
            head = head.next
        
        # need to cut the end of the lists
        odds.next = None
        evens.next = None
        
        if odds:
            odds.next = evenHead.next
            return oddHead.next
        else:
            return evenHead.next


'''
clear
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #edge cases: empty first node, one node, two nodes,
        # make two LL (odd-only, even-only) in one pass, then append even on end of odd and return head of odd
        # time: O(n)
        # space: O(1)
        
        if head is None or head.next is None or head.next.next is None:
            return head
        
        odd,even = head,head.next
        evenStart = even
        
        # create two LL
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        # append even LL to end of odd LL
        odd.next = evenStart
        
        # return head of even
        return head

