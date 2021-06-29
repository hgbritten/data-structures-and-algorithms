# from code_challenges.tree.tree import Node, Queue, BinarySearchTree, BinaryTree
from code_challenges.hashtable.hashtable import Hashtable


def tree_intersection(bt1, bt2):
    new_arr = []
    tree1 = bt1.pre_order()
    tree2 = bt2.pre_order()
    ht = Hashtable()
    for value in tree1:
        ht.add(key=str(value), value=value)
    for value in tree2:
        if ht.contains(str(value)):
            new_arr.append(value)
    return new_arr
