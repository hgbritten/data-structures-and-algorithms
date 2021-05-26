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


# We want a leader variable to start at the head. We want to initialize a follower variable. We also want to initialize a paces variable that knows how many places back the follower is from the leader. In order to traverse through the list we use a while loop.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
