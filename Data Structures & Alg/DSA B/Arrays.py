class DynamicArray:
    def __init__(self):
        self.array = [0] * 3
        self.count = 0

    def insert(self, item):
        if self.count == len(self.array):
            new_array = [0] * (len(self.array) * 2)
            for i in range(len(self.array)):
                new_array[i] = self.array[i]
            self.array = new_array
        self.array[self.count] = item
        self.count += 1

    def remove(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.count - 1] = 0
        self.count -= 1

    def print_array(self):
        for i in range(self.count):
            print(self.array[i])

# Uso do DynamicArray
arr = DynamicArray()
arr.insert(10)
arr.insert(20)
arr.insert(30)
arr.print_array()
arr.remove(1)
arr.print_array()
