# ALGORITHM Mergesort(arr)
#     DECLARE n <-- arr.length

#     if n > 1
#       DECLARE mid <-- n/2
#       DECLARE left <-- arr[0...mid]
#       DECLARE right <-- arr[mid...n]
#       // sort the left side
#       Mergesort(left)
#       // sort the right side
#       Mergesort(right)
#       // merge the sorted left and right sides together
#       Merge(left, right, arr)

# ALGORITHM Merge(left, right, arr)
#     DECLARE i <-- 0
#     DECLARE j <-- 0
#     DECLARE k <-- 0

#     while i < left.length && j < right.length
#         if left[i] <= right[j]
#             arr[k] <-- left[i]
#             i <-- i + 1
#         else
#             arr[k] <-- right[j]
#             j <-- j + 1

#         k <-- k + 1

#     if i = left.length
#        set remaining entries in arr to remaining values in right
#     else
#        set remaining entries in arr to remaining values in left


def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    if n > 1:
        mid = n // 2
        left = lst[0:mid]
        right = lst[mid:n]
        merge_sort(left)
        merge_sort(right)
        return merge(left, right, lst)


def merge(left, right, lst):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1
        k = k + 1
    if i == len(left):
        lst[k:] = right[j:]
    else:
        lst[k:] = left[i:]
    return lst
