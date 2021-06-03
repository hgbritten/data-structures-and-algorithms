from code_challenges.stacks_and_queues.invalid import InvalidOperationError


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        """This enqueue is for Queue and requires a value"""
        if self.rear:
            self.rear = Node(value)
        else:
            self.rear = Node(value)
            self.front = self.rear

    def dequeue(self):
        if self.front:

            temp = self.front
            self.front = self.front.next
            temp.next = None

            return temp.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")


# class AnimalShelter:
#     def __init__(self):
#         self.shelter = Queue()

#     # ToDO
#     # enqueue and dequeue methods
#     # preferred method for pref cat or dog that returns null if none is selected

#     def enqueue(self, pet):
#         """Enqueue for AnimalShelter class requires a pet to be passed in"""
#         self.shelter.enqueue(pet)

#     def dequeue(self, pref):
#         if not pref in ["dog", "cat"]:
#             return None
#         pet = None
#         front = None
#         current = self.shelter.dequeue()
#         while current != front:
#             front = front or current
#             if self.pref_check(pref, current):
#                 if current == front:
#                     return current
#                 pet = pet or current
#             self.shelter.enqueue(current)
#             current = self.shelter.dequeue()
#         return pet

#     def pref_check(self, pref, pet):
#         if pref == "cat":
#             thing_to_dequeue = Cat
#         elif pref == "dog":
#             thing_to_dequeue = Dog
#         return isinstance(thing_to_dequeue, object)


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        else:
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog" and self.dogs:
            return self.dogs.dequeue()
        if pref == "cat" and self.cats:
            return self.cats.dequeue()

        return None


class Dog:
    def __repr__(self):
        return "dog"


class Cat:
    def __repr__(self):
        return "cat"
