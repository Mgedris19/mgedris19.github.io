# The beginning.
 
There is a pretty good chance that you have worked
with lists in the past.  Well a stack is kind of
like a list, with a few more steps to it.
 
## Real world example.
Pancakes.  Or creps, waffles, tortillas, or well
you get the idea.  A stack is just a stack of data
that you perform operations on.  But how you perform
them matters.  While technically you can grab a
pancake from anywhere in the stacks, that generally
is looked down on by our society.  The same is true for
stacks.  You can grab items from the middle of the
stack, but it isn't good practice.  So with a stack
the idea is what is called first in first out, or
FIFO.  The first item in the stack is also the first
time off of the stack.
 
## Image of how this works and explanation
[A simple stack](stack.PNG)
 
The image might be a little weird when you first look
at it so let's see what's going on.  In the first
image we have an empty stack and six objects that
aren't on it so the second image shows the first
object being called onto the stack and is at the
bottom of the stack.  The next image shows the rest
of the objects being called onto the stack, and then
filled in according to numerical order.  The stack
is now complete and we have numbers descending in
order 6 to 1.  When we want to call off the number
in the stack we look at the fourth image.  The stack
calls off the first number that is in order.  In
terms of python functions, this would be.
```python
list.pop()
```
## O notation for stacks
[O of stack functions](Stack_O.PNG)
 
 
## Example time!
In this example of a stack what we are doing is
adding onto a stack and then taking all of the items
off again.  Sounds simple enough, so let's take a
look at how I would do it.  In this instance we are
going to be making a function that will take in a
list and then put it on a stack.
 
```python
def stack_on (list):
    stack=[]
    for x in list:
        stack.append(x)
    print(stack)
```
 
Okay great we can now add things onto a stack, but
how do we take things off of one?  Well like I said
above because this is basically a list there is already
a built in function to help us out: pop.
Let's see what an example might look like.
 
```python
def stack_off (stack):
    while len(stack) != 0:
        print(stack.pop())
```
That's it, it is that simple.
 
## Challenge:
Alright now it's time for you to take the reins.  For
this challenge make a function that creates a stack from
a list but every other time it adds an item take that
item off the stack.  Then when there are no more items
in the list print the stack.  Think of this as just
making a stack of all the odd indexed variables in
a list.
 
Here is the solution for when you are finished.
 
[Stack solution](stack_solution.py)
 
[Linked lists](Linked_lists.md)
 
[Trees](Trees.md)
 

