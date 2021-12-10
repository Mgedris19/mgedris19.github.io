# TREES!
 
Probably not what you are thinking.  No these are not the
trees that you go outside and look at.  Rather these are
data trees.  If you have already looked at and gone through
the linked list tutorial, trees are very similar the
biggest difference between them is that trees are sorted.
 
If you haven't gone through the tutorial and want to here
is the link to it.
[Linked lists](Linked_Lists.md)
 
If you've gone through it already, or just don't want to,
lets get rolling with trees.
 
## What's the difference?
The biggest difference between linked lists and trees are
how they are stored/sorted.  Linked lists have no sort to
them while trees have a sort to them similar to a binary
sort.  The biggest difference between a binary sort and a
tree is how it would look, so get a visual to help out.
One quick thing to note is that there will occasionally in
this tutorial the letters BST, no this is not the K-pop
band, this is an abbreviation for the words "Binary search
tree", the full name for trees.
 
[A tree](Tree.PNG)
 
So with this, the "head node" (or root) is the number 8 and
then it there are two more underneath it, which is be true
for all of the nodes even if you don't see them.  Like in \
the nodes with the numbers 1,7,9,and 14.  Numbers 1 and 9
don't have any nodes underneath them.  But there are still
nodes there that aren't being used yet.  But 3 and 10 have
nodes to the left, but nothing on the right.  Nonetheless
there are still nodes there.  So with each nod having two
"children".  The node that is off to the left will always
be less than node above it, and the node to the right will
be greater than the node above it.
 
## Big O of trees
[O of tree functions](Tree_o.PNG)
 
## Additional information
Working with trees, can sometimes be a nightmare.  I say
this because these things can get messy, and by that I mean
the tree can get unbalanced.  The tree in the example I
gave was a balanced tree(there were roughly the same
amount of nodes on each side of the tree.) but an
unbalanced tree is when there is an imbalance in the data.
An unbalanced tree looks like this.
 
[unbalanced](unbalance.PNG)
 
From this image what is happening is that there is too much
data on the right side of the tree.  The reason that this
becomes a problem is because at this point it is basically
a linked list.  Now this isn't a bad thing persay, but
it isn't what we had in mind when doing this.  The reason
that trees get used is because of Big O.  For trees the
Big O notation is significantly smaller than linked lists.
 
When you get a tree that is unbalanced there are a few
third party websites and browsers that help balance out the
tree again.
 
## Making it work
All things considered, trees are pretty simple and work
similar to linked lists.  Two things that are different
are first: that the data really should be sorted before
you put it in a tree.  The second and biggest thing is you
have to do is determine if the node being added in is less
than or greater than the node the program is looking at.  
To do this we need a little friend called recursion.
 
## Recursion
Recursion is when something calls itself.  Like when you
google what is recursion.  If you haven't tried this it
is rather amusing.  So for trees to work there needs to be
a recursive call that is called to see if the nodes being
added in are less than or greater than the current node
the function is looking at.  If the node is less than
the current node, then check to see if there is a node
occupying that spot already.  If not then place the new
node there.  We will do the same thing for if the node is
greater than it.  If there is something there already then
we need to call the function again only the new node to
look at will be one of the ones on the left.  One last
thing that we should address is that we really only want
one copy of each piece of data.
 
## Let's take a look
Here is an example of how you could set up the insert
function of a tree.
 
```python
def _insert(self, data, node):
        """
        This function will look for a place to insert a
        node with 'data' inside of it.  The current
        sub-tree is represented by 'node'.  This function
        is intended to be called the first time by the
        insert function.
        """
        if data==node.data:
            return False
        else:
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot
                    node.left = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the left sub-tree.
                    self._insert(data, node.left)
            else:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot
                    node.right = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the right sub-tree.
                    self._insert(data, node.right)
 
 
```
 
For this problem it is important to note that this
function is part of a class as python doesn't have a
tree class by default.
 
For this next one you are going to see what needs to be
done if you want to go through the tree to see what data is
in there.  Only instead of going forward for the data,
you will be going backward.
 
```python
def __reversed__(self):
        """
        Perform a forward traversal (in order traversal)
        starting from the root of the BST.  This function
        is called when a the reversed function is called
        and is frequently used with a for loop.
        """        
        yield from self._traverse_backward(self.root)  
        #Start at the root node
        #This is called as the first traversal function.  
 
    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order
        traversal) through the tree.  If the node that we
        are given (which is the current sub-tree) exists,
        then we will keep traversing on the right side
        (thus getting the larger numbers first), then we
        will provide the data in the current node, and
        finally we will traverse on the left side (thus
        getting the smaller numbers last).  This function
        is intended to be called the first time by the
        __reversed__ function.        
        """
 
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
```
 
## Challenge time
Alright for one last time in this guided tutorial, you are
incharge again.  For this challenge take what you've seen
with the iteration of a tree backward, and instead go
forward with it.  For this to work you will need a little
bit more code to work with.  So here is the start file.
 
[tree start](tree_start.py)
 
When you are done, here is the solution for the problem.
 
[tree answer](tree_solution.py)
 

