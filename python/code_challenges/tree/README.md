# Trees
<!-- Short summary or background information -->
- Trees are sort of like queues and stacks where they store information in Nodes. However trees know more information and can be traversed in a lot of different ways which can be extremely beneficial.
## Challenge
<!-- Description of the challenge -->
- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node. Then create preorder, postorder, and inorder traversal methods
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- My approach was to use what we learned in class to build a preorder def. I think the Big O for this is n
## API
<!-- Description of each method publicly available in each of your trees -->
- I don't have an API for this
- Link https://github.com/hgbritten/data-structures-and-algorithms/compare/tree?expand=1


# Breadth First
<!-- Description of the challenge -->
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.
## Whiteboard Process
<!-- Embedded whiteboard image -->
[breadth_first](breadth_first.PNG)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- our approach was to use the provided pseudocode to make the breadth_first method. Then we just had to change up the enque and dequeue methods and use deque instead of what we had previously been doing.
## Solution
<!-- Show how to run your code, and examples of it in action -->
- Check out our tests in test_tree.py
- link https://github.com/hgbritten/data-structures-and-algorithms/pull/29
