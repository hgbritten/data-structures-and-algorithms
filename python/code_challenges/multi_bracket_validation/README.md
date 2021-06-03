# Challenge Summary
<!-- Description of the challenge -->
- With help from Tim Viccari
- Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets: () [] {}
## Whiteboard Process
<!-- Embedded whiteboard image -->
[multi_bracket_validation](multi_bracket_validation.PNG)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- We took the approach of spliting the string up into individual strings and checking each string for an opening or closing parens. We set up values for each of the bracket types and if it ever reaches below 0 aka a ), }, ] comes before a (, {, [ we return False and if the values aren't 0 at the end for all of the values we return false.
- The BigO for us is O(n) for the length of the list
## Solution
<!-- Show how to run your code, and examples of it in action -->
- Solution for this one is pretty easy. Just test out different strings with different combos of brackets and expect either true or false
