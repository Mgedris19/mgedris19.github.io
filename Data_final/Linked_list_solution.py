class LinkedList:

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        new_node=LinkedList.Node(value)

        #If the list is empty point both head and tail to new node.  Other wise only the .tail will change
        if self.tail is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node