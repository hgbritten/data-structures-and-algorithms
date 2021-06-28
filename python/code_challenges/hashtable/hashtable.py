class Hashtable:
    def __init__(self, size=1024):
        self._buckets = [None] * size

    def add(self, key, value):
        index = self.hash(key)
        if not self._buckets[index]:
            self._buckets[index] = LinkedList()

        self._buckets[index].insert([key, value])

    def get(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]
        if not bucket:
            return None

        current = bucket.head

        while current:
            if current.value[0] == key:
                return current.value[1]
        return None

    def contains(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            return False

        current = bucket.head

        while current:
            if current.value[0] == key:
                return True
            current = current.next

        return None

    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        sum *= 19

        index = sum % len(self._buckets)

        return index


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in reversed(values):
                self.insert(value)

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        output_string = ""
        current = self.head
        while current:
            output_string += f"{current.value} -> "
            current = current.next
        output_string += "None"
        return output_string

    def to_list(self):
        values = []

        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values

    def append(self, value):
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(value, current.next)
                break
            else:
                current = current.next

    def insert_before(self, value, new_val):
        current = self.head
        if self.head.value == value:
            self.head = Node(new_val, self.head)
        else:
            while current:
                if current.next.value != value:
                    current = current.next
                else:
                    current.next = Node(new_val, current.next)
                    break

    def insert_after(self, value, new_val):
        current = self.head
        while current:
            if current.value != value:
                current = current.next
            else:
                current.next = Node(new_val, current.next)
                break

    def k(self, k):
        follower = None
        leader = self.head
        paces = 0
        while leader:
            leader = leader.next
            if follower:
                follower = follower.next
            elif paces == k:
                follower = self.head
            else:
                paces += 1
        return follower.value


def zip_lists(list_1, list_2):
    current1 = list_1.head
    current2 = list_2.head
    while current1 and current2:
        next_1 = current1.next
        next_2 = current2.next
        current1.next = current2
        if next_1:
            current2.next = next_1
            current1 = next_1
            current2 = next_2
        else:
            break
    return list_1


# We want a leader variable to start at the head. We want to initialize a follower variable. We also want to initialize a paces variable that knows how many places back the follower is from the leader. In order to traverse through the list we use a while loop.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
