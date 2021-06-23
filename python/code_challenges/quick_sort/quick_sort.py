# quick_sort order of leaving the stack
# [0,-1] quick_sort(lst, left, position - 1) call 3
# [1,1] quick_sort(lst, position +1, right) call 4
# [0,1] quick_sort(lst, left, position - 1) call 2
# [3,3] quick_sort(lst, left, right) call 6
# [5,5] quick_sort(lst, position +1, right) call 7
# [3,5] quick_sort(lst, position +1, right) call 5
# [0,5] quick_sort(lst, left, right) call 1
#
#
#


def quick_sort(lst, left, right):
    if left < right:
        position = partition(lst, left, right)
        quick_sort(lst, left, position - 1)
        quick_sort(lst, position + 1, right)
    return lst


def partition(lst, left, right):
    pivot = lst[right]
    low = left - 1
    for i in range(left, right):
        if lst[i] <= pivot:
            low += 1
            swap(lst, i, low)
    swap(lst, right, low + 1)
    return low + 1


def swap(lst, i, low):
    temp = lst[i]
    lst[i] = lst[low]  # 23 = 42
    lst[low] = temp


# [8,4,23,42,16,15] very first partition call
# [8,4,15,42,16,23] ^^^^
# ----------second partition call
# [4,8,15,42,16,23]^^^^^^
#

# left = 3, right = 5
# pivot = 23
# low 5
# i 3


# Sample Lists
# [8,4,23,42,16,15]
# [2,3,5,7,13,11]
# [5,12,7,5,5,7]
# [20,18,12,8,5,-2]
print(quick_sort([8, 4, 23, 42, 16, 15], 0, 5))
