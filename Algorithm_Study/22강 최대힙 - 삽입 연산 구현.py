class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item);
        i = len(self.data) - 1

        while i // 2 > 0 and self.data[i // 2] < self.data[i]:
            self.data[i // 2],self.data[i] = self.data[i], self.data[i // 2]
            i = i // 2



def solution(x):
    return 0