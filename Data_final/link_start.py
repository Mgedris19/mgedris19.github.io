class LinkedList:
    class Node:
       """
       Each node of the linked list will have data and 
       links to the previous and next node. 
       """

       def __init__(self, data):
           """ 
           Initialize the node to the data provided.  
           Initiallythe links are unknown so they are set 
           to None.
           """
           self.data = data
           self.next = None
           self.prev = None
    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node
    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """

        if self.head==self.tail:
            self.head=None
            self.tail=None
        elif self.tail is not None:
            self.tail.prev.next=None
            self.tail=self.tail.prev
