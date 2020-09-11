# Description: Min Heap implementation


# Import pre-written DynamicArray and LinkedList classes
from include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        adds a value to the Min Heap
        :param node: object
        :return: None
        """
        # place node at bottom of the tree, swap with parent nodes until correct placement found
        self.heap.append(node)
        cur = self.heap.length() -1
        while cur > 0:
            if self.heap.get_at_index(cur) < self.heap.get_at_index(int((cur-1)/2)):     # child > parent?
                self.heap.swap(cur, int((cur-1)/2))                                      # swap
                cur = int((cur-1)/2)
                continue
            break

    def get_min(self) -> object:
        """
        returns the min value from the heap. raises exception if heap is empty
        :return: object
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        removes and returns the min value from the heap
        :return: None
        """
        if self.is_empty():
            raise MinHeapException
        elif self.heap.length() == 1:
            return self.heap.pop()

        # place the last node at top of tree, swap nodes downward until correct placement found
        min = self.heap.get_at_index(0)
        self.heap.set_at_index(0, self.heap.pop())
        cur = 0

        # while there is at least one child
        while 2*cur+1 < self.heap.length():

            # both children exist
            if 2*(cur+1) < self.heap.length():

                # swap with right child
                if self.heap.get_at_index(2*cur+1) >= self.heap.get_at_index(2*(cur+1)) and \
                   self.heap.get_at_index(cur) > self.heap.get_at_index(2*(cur+1)):
                    self.heap.swap(cur, 2*(cur+1))
                    cur = 2*(cur+1)

                # swap with left child
                elif self.heap.get_at_index(2*cur+1) <= self.heap.get_at_index(2*(cur+1)) and \
                     self.heap.get_at_index(cur) > self.heap.get_at_index(2*cur+1):
                    self.heap.swap(cur, 2*cur+1)
                    cur = 2*cur+1
                else:
                    break

            # only left child exists
            else:
                if self.heap.get_at_index(cur) > self.heap.get_at_index(2*cur+1):
                    self.heap.swap(cur, 2*cur+1)
                break

        return min

    def build_heap(self, da: DynamicArray) -> None:
        """
        builds a min heap from an array at O(n)
        :param da: DynamicArray object
        :return: None
        """

        # find the first non-leaf node
        cur = da.length()-1
        while 2*cur+1 >= da.length() and 2*(cur+1) >= da.length():
            cur -= 1

        # swap pairs to bubble up the smallest children
        while cur >= 0:

            # both children exist
            if 2*(cur+1) < da.length():

                # swap with right child
                if da.get_at_index(2*cur+1) > da.get_at_index(2*(cur+1)) and \
                   da.get_at_index(cur) > da.get_at_index(2*(cur+1)):
                    da.swap(cur, 2*(cur+1))

                # swap with left child
                elif da.get_at_index(2*cur+1) < da.get_at_index(2*(cur+1)) and \
                    da.get_at_index(cur) > da.get_at_index(2*cur+1):
                    da.swap(cur, 2*cur+1)

            # only left child exists
            else:
                if da.get_at_index(cur) > da.get_at_index(2*cur+1):
                    da.swap(cur, 2*cur+1)
            cur -= 1


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)