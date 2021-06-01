# Challenge Summary
<!-- Description of the challenge -->
- Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the enqueue and dequeue values

## Whiteboard Process
<!-- Embedded whiteboard image -->
[queues-with-stacks](queues-with-stacks.PNG)
- Made with Brian L and Skyler J

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- We took the approach of using the two stacks to achieve different goals. The "left" stack is for enqueuing and the "right" stack is for dequeuing. If you are switching between the two you need to move the stack to the other stack using push and pop so they are in the correct order to follow first in first out.

## Solution
<!-- Show how to run your code, and examples of it in action -->
- If you can see the tests and see everything is passing you are good to go. There may be other ways to test, but I think I covered everything.

### Link
- https://github.com/hgbritten/data-structures-and-algorithms/pull/24
