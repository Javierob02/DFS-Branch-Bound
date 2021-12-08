from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room

    def estimate(self, items):
        bound = 0
        for i in range(self.index, len(items)):
            item = items[i]
            bound += item.value
        result = self.value + bound
        return result