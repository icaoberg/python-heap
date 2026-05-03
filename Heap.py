from Node import Node
import random

class MinHeap:
    def __init__(self):
        self._data = []

    def random(self, number_of_nodes):
        self._data = []
        if number_of_nodes <= 0:
            return
        elements = random.sample(range(number_of_nodes), number_of_nodes)
        for e in elements:
            self.push(e)

    # --- index helpers ---

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    # --- heap maintenance ---

    def _sift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self._data[i].get() < self._data[p].get():
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self._data)
        while self._has_left(i):
            smallest = self._left(i)
            if self._has_right(i) and self._data[self._right(i)].get() < self._data[smallest].get():
                smallest = self._right(i)
            if self._data[smallest].get() < self._data[i].get():
                self._swap(i, smallest)
                i = smallest
            else:
                break

    # --- public interface ---

    def push(self, element):
        self._data.append(Node(element))
        self._sift_up(len(self._data) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._data) - 1)
        node = self._data.pop()
        if self._data:
            self._sift_down(0)
        return node.get()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self._data[0].get()

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def tolist(self):
        return [node.get() for node in self._data]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"MinHeap({self.tolist()})"


class MaxHeap:
    def __init__(self):
        self._data = []

    def random(self, number_of_nodes):
        self._data = []
        if number_of_nodes <= 0:
            return
        elements = random.sample(range(number_of_nodes), number_of_nodes)
        for e in elements:
            self.push(e)

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self._data[i].get() > self._data[p].get():
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self._data)
        while self._has_left(i):
            largest = self._left(i)
            if self._has_right(i) and self._data[self._right(i)].get() > self._data[largest].get():
                largest = self._right(i)
            if self._data[largest].get() > self._data[i].get():
                self._swap(i, largest)
                i = largest
            else:
                break

    def push(self, element):
        self._data.append(Node(element))
        self._sift_up(len(self._data) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._data) - 1)
        node = self._data.pop()
        if self._data:
            self._sift_down(0)
        return node.get()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self._data[0].get()

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def tolist(self):
        return [node.get() for node in self._data]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"MaxHeap({self.tolist()})"
