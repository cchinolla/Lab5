import math


class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


class DoublyLink:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        temp = self.tail
        temp.next = new_node
        new_node.prev = temp
        self.tail = new_node
        new_node.next = None

    def delete_at_start(self):
        if self.head is None:
            print("empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        temp = self.head
        temp.prev = None

    def relocate(self, node):
        if node == self.tail:
            return
        if node == self.head:
            n = self.head.next
            n.prev = None
            self.head = n
            self.insert_at_end(node)
        else:
            temp = node.prev
            temp.next = node.next
            tt = node.next
            tt.prev = temp
            self.insert_at_end(node)


class LRU:
    def __init__(self, cap):
        self.LRU = {}
        self.cap = cap
        self.list = DoublyLink()
        self.size = 0
        print("hey")

    def get(self, key):
        if key in self.LRU:
            self.list.relocate(self.LRU[key])
            return self.LRU[key]
        else:
            return -1

    def put(self, key, value):
        print("hi")
        node = Node(value, key)
        if key not in self.LRU:
            if self.size != self.cap:
                self.list.insert_at_end(node)
                self.size += 1
            else:
                self.list.delete_at_start()
                self.list.insert_at_end(node)
        else:
            self.list.relocate(self.LRU[key])
            self.list.tail.value = value

    def sizeA(self):
        return self.size

    def max_capacity(self):
        return self.cap

    def printl(self):
        x = self.list.head
        while x is not None:
            print(x.key, x.value)
            x = x.next


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -math.inf
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):

        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)


def heap_sort(a_lst):
    h = MaxHeap()
    for a in a_lst:
        h.insert(a)
    # print(h.tree)
    i = 0
    while not h.is_empty():
        a_lst[i] = h.extract_max()
        i = i+1


def most_freq(string, k):
    dict = {}
    listt = list()
    # stuff = list()
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 1
        else:
            dict[string[i]] = 1
    for value in dict.values():
        listt.append(value)
    heap_sort(listt)
    print(listt)

    final = []
    i = 0
    while i < len(listt):
        for j in dict:
            if listt[j] == dict[i]:
                final.append(j)
                i = i+1
    for i in range(k):
        print(final[i])
    # print(list)


def main():
    # a = LRU(3)
    # a.put("A", 2)
    # a.put("B", 6)
    # a.put("C", 8)
    # a.put("nancy", 9)
    # a.put("j", 6)
    # a.put("k", 8)
    # a.printl()

    c = ["sup", "hi", "cat", ":)", "joe", "cat","cat", "joe"]
    most_freq(c, 2)


main()
