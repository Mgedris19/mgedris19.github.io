# Data Structures final
## Stacks, Linked lists and Trees.
 
Just what are these things?
Well, let's take a look.
 
## A Stack
This is just what it sounds like, a stack of data.
Completely  unorganized data that is just stuck on
top of each other, Figuratively speaking.  
[stack page](stack.md)
 
## A linked list
The easiest way to introduce this is to think
of this as a list that is floating around in
memory somewhere.  The difference is that the
pieces of data are still connected.
[Linked list](Linked_lists.md)
# Linked lists:
Okay so you've likely worked with lists in the past, so
what is the difference between a normal list and a linked
list then?  Well this mostly just has to deal with 
storage and locations in memory.  Now in python this 
doesn't matter that much as pointers aren't really a 
thing..... or so you thought.  Imagine if you will a 
large open area of water and in it there are some 
jellyfish that are floating about and some of the 
tentacles are touching the heads of another jelly.
This is kind of a linked list, but instead of a body of
water and jelly fish, it's the memory of your computer 
and objects that are part of a list.  For reference this
function has a big O notation of n, as it has to loop 
through all of the possible indexes.
 
## How it works
In this instance every member of the list are called
nodes, as such each node has three parts to it: the 
head, the body, and the tail.  The body of the node is
where all of the data is stored, we don't really don't 
care about that part for this example, the head and
tail are what we are going to focus on.  The head of 
the node "points" to the node that is before that node, 
and the tail "points" to the node that is after it.  
Here is how it would look.
 
 [Linked list](linked-list.PNG)
 
 ## What the image is representing
 The image might be a little confusing, but in short here 
 is what is happening.  The first node in the list is first
 thing in memory, after some random data that came from
 somewhere, there are two more nodes in the linked list.  
 These nodes are still linked to the first node, because
 the the "tail" of the first node is pointing to the 
 "head" of the second node, and so on so forth to the
 next node.  This continues until there are no more
 nodes in the data set.
 
## O of linked lists
[O Linked list functions](Linked_list_O.PNG)
 ## A little more about linked lists
 As I mentioned above the nodes have a head and a tail 
 which point to each other (head to tail and tail to 
 the next head).  For the first node though there won't be
 a place for the head to point to, so it would just be set
 to none.  The same is true for the last item in the 
 linked list, the tail will be set to none.
 
 # Example of a node
 ```python
     class Node:
        """
        Each node of the linked list will have data and 
        links to the previous and next node. 
        """
 
        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  
            Initially the links are unknown so they are set 
            to None.
            """
            self.data = data
            self.next = None
            self.prev = None
 ```
 
 However a node doesn't work just by itself, so there 
 has to be another thing that connects allows it to work,
 for this we will also need to create our own as there
 isn't anything built into python to help us out here.
 
 ```python
 class linked_list:
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
            self.head = new_node  # Update the head to point to the new node
 ```
 
## Example time.
 
Alright so let's start out by having there be an insert 
a node to the beginning of the linked list class.  Normally 
when inserting, you do it at the end of the list, but for this one we are going to put it at the beginning.
```python
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
```
 
The next thing will be doing is taking off the tail or 
last node of the list.  This is an example of what it 
could look like.
```python
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
 
        pass
```
<!--  -->
 
## Challenge
Alright you are incharge again and this time I want you to
take what you learned/saw in the examples and flip it.
So take the insert_head function and make it insert to the
tail of the linked list.  And for the remove tail make it 
a remove head function.  Here is a startup file to help
you out a little.
 
[Linked list start](link_start.py)
 
Put the solution here when it's finished.
 
When you are finished with these projects the next step to
take is going to be taking on data trees.
 
[Data trees](Trees.md)
## A Tree
In short this is a linked list with a few more steps
to it.  The data is organized off of a single piece
of data.
[Trees](Trees.md)
 
## Continue?
The data structures are set, are you ready to begin
the journey into the world of data structures?
 
[Yes](stack.md)
 
[No](no.md)
 

