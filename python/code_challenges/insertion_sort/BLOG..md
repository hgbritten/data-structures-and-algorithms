# Insertion Sort

##### Insertion Sort is a sorting algorith that traverses the list one time and as it does it checks the values in front of the current value and moves them into ascending order.

## Pseudocode
[insertion](insertion.PNG)


## Trace
##### Sample List: [20, 18, 8, 12, 5, -2]

[Pass1](pass1.PNG)

##### In the first loop through the insertion sort, we pay attention to i at position 1. Then we check the value of i at 0 against the value of i at one. If i at 1 is less than i at 0 they switch places.

[Pass2](pass2.PNG)

##### On the second loop through the list we move our focus to i at position 2. Then while i at position 2 is less than i at the position in front of it we move down the list. The value in position one in this case would move to position 2 and 2 would move down to one. This process repeats and 2 eventually gets to position 0.

[Pass3](pass3.PNG)

##### On this next loop through the list we move to i at position 3 and check the values at the positions infront of them. The value at position 3 breaks the while loop once it sees a lower number at position 0 in the list.

# Efficency
- Time: O(n^2)
      - The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times... concluding the algorithm to be n squared.

- Space O(1)
      - No additional space is being created. This list is being sorted in place... keeping the space at a constant O(1).
