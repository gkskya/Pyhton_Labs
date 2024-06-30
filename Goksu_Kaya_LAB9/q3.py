import random
import time

class HeapSort:
    def init(self, data):
        self.data = data
        self.heapified = self.heapify()
        self.sorted = self.sort()

    def heapify(self):
        for i in range(len(self.data)//2, 0, -1):
            self.downheapify(i, len(self.data)-1)
        return self.data

    def downheapify(self, parent, last):
        temp = self.data[parent]
        while parent*2 <= last:
            child = parent*2
            if child != last and self.data[child] < self.data[child+1]:
                child += 1
            if temp >= self.data[child]:
                break
            self.data[parent] = self.data[child]
            parent = child
        self.data[parent] = temp

    def sort(self):
        for last in range(len(self.heapified)-1, 0, -1):
            self.heapified[1], self.heapified[last] = self.heapified[last], self.heapified[1]
            self.downheapify(1, last-1)
        return self.heapified


data = [random.randint(1, 100) for _ in range(25)]
print(f"Initial Array: {data}")

start = time.time()
heapSort = HeapSort([0] + data)
end = time.time()

print(f"Heapified Array: {heapSort.heapified}")
print(f"Sorted Array: {heapSort.sorted}")
print(f"Seconds {end - start:.15f}")
