# Linked lists:
Okay so you've likely worked with lists in the past, so
what is the differnce between a normal list and a linked
list then?  Well this mostly just has to deal with 
storage and locations in memory.  Now in python this 
doesn't matter that much as pointers aren't really a 
thing..... or so you thought.  Imagine if you will a 
large open area of water and in it there are some 
jelly fish that are floaging about and some of the 
tenticles are touching the heads of another jelly.
This is kind of a linked list, but instead of a body of
water and jelly fish, it's the memory of your computer 
and objects that are part of a list.

## How it works
In this instance every member of the list are called
nodes, as such each node has three parts to it: the 
head, the body, and the tail.  The body of the node is
where all of the data is stored, we don't really don't 
care about that part for this example, the head and
tail are what we are going to focus on.  The head of 
the node "points" to the node that is before that node, 
and the tail "points" to the node that is after it.  
