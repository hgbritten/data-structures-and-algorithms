class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.values = values

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


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
