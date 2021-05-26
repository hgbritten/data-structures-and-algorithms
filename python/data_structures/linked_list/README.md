# Challenge 5

# Singly Linked List
<!-- Short summary or background information -->
A singly linked list is a list that only points to one other node. It only has its own value and the address for the next node
## Challenge
<!-- Description of the challenge -->
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The Big O is O(1)!

## API
<!-- Description of each method publicly available to your Linked List -->
- https://github.com/hgbritten/data-structures-and-algorithms/pull/19

# Challenge 6

# Extend a Linked List to allow various insertion methods

<!-- With help from Brian L -->

<!-- https://github.com/hgbritten/data-structures-and-algorithms/pull/20 -->

## Challenge Summary
Add new methods to Linked List class
- .append(value)
- .insertBefore(value, newVal)
- .insertAfter(value, newVal)

## Whiteboard Process
[11-insertion](./11-insertion.PNG)

## Approach & Efficiency
- Our approach to this one was to write test for all the parts of the methods we were adding and being sure of what they were doing.
- Append has a big O(n)
- insert before and after have a big 0(1)

# Solution
<!-- Show how to run your code, and examples of it in action -->
- Run the code with pytest and check them out in test_linked_list.py

## Challenge Summary
Add new method to find k from the end's position value

## Whiteboard Process
[11-kth-from-end](./11-kth-from-end.PNG)

## Approach & Efficiency
- Our approach to this was to write a method that followed the leader down by k positions to get the value at the k index provided.
- this has a big O(n) depending on the length of the list

# Solution
- Run the code with pytest and check them out in test_linked_list.py
