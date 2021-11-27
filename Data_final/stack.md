# The beginging.

There is a pretty good chance that you have worked
with lists in the past.  Well a stack is kind of 
like a list, with a few more steps to it.

## Real world example.
Pancakes.  Or creps, waffels, tortilas, or well
you get the idea.  A stack is just a stack of data
that you perform opperations on.  But how you perform
them matters.  While technically you can grab a
pancake from anywhere in the stacks, that generaly
is looked down on our society.  The same is true for
stacks.  You can grab items from the middle of the 
stack, but it isn't good practice.  So with a stack 
the idea is what is called first in first out, or 
FIFO.  The first item in the stack is also the first
itme off of the stack.

## Image of how this works and explination
[A simple stack](stack.PNG)

The image might be a little weird when you first look 
at it so let's see what's going on.  In the first 
image we have an empty stack and six objects that 
aren't on it so the second image shows the first 
object being called onto the stack and is at the 
bottom of the stack.  The next image shows the rest
of the objects being called onto the stack, and then
filled in according to numerical order.  The stack 
is now complete and we have numbers decending in 
order 6 to 1.  When we want to call off the number 
in the stack we look at the fourth image.  The stack
calls off the first number that is in order.  In 
terms of python functions, this would be.
```python
list.pop()
```

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
        stack.append(list[x])
    print(stack)
```
<!-- When we run this function we get an error, take a 
look at it when we get back onto the wifi, before 
we submit it.  Index is out of range. -->

 Okay great we can now add things onto a stack, but
 how do we take things off of one?  Well like I said
 above because this is basicaly a list there is already
 a built in function to help us out: pop.
Let's see what an exxample might look like.

```python
def stack_off (stack):
    for x in stack:
        stack.pop()
        print(stack)
```
That's it, it is that simple.

<!-- 
We've got something weird going on with the above
example.  It sees the first few items and then decides
to stop going after about three run throughs.
-->

## Challenge:
Alright now it's time for you to take the reings.  For 
this challenge make a function that creates a stack from
a list but every other time it adds an item take that 
item off the stack.  Then when there are no more itmes 
in the list print the stack.  Think of this as just 
making a stack fo all the odd indexed variables in 
a list.

