import typing

class ListNode:
    def __init__(self, val:int, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head: typing.Optional[ListNode]) -> None:
        self._head = head

    def merged_sorted(self, l2) -> None:
        """ v
            8 -> 15 -> 19 -> null
            9 -> 10 -> 16 -> null
            ^     
        dummy -> 4 -> 7 -> None
                    merg
        """       
        
        dummy = ListNode(val=-1)
        merged = dummy
        head1 = self._head
        head2 = l2.head

        while head1 and head2:
            if head1.val <= head2.val:
                h1_next = head1.next
                merged.next = head1
                head1 = h1_next
            else:
                h2_next = head2.next
                merged.next = head2
                head2 = h2_next

            merged = merged.next
            merged.next = None

        if head1:
            merged.next = head1
        elif head2:
            merged.next = head2

        self._head = dummy.next

    def invert_list(self, head: ListNode):
        """
        3 -> 5 -> 8 -> 15 -> 19 -> null

        5 -> 3 -> null

        curr = 5
        
        19 -> 15 -> 8 -> 5 -> 3 -> null

        """
        prev = None 
        next = head.next # 5
        curr = head # 3

        while curr:
            curr.next = prev # 19 -> 15 -> 8 -> 5 -> 3 -> null, 8 -> 15 -> 19 -> null
            prev = curr # prev = 19 
            curr = next # curr = none
            next = next.next if next else None
        
        return prev

    def print_list(self):
        iter = self._head
        while iter:
            if iter.next:
                print(str(iter.val) + " -> ", end=''),
            else:
                print(str(iter.val) + " -> null")
            iter = iter.next
