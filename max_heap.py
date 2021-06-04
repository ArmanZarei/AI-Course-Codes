import math 

class Heap:
    def __init__(self, max_size, type='max'):
        self.heap = [0 for _ in range(max_size + 1)]
        self.size = 0
        self.max_size = max_size
        self.type = type
        self.heap[0] = math.inf if self.type == 'max' else -math.inf
    
    def __parent(self, pos):
        return pos//2
    
    def __left_child(self, pos):
        return 2*pos
    
    def __right_child(self, pos):
        return 2*pos + 1
    
    def __swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]
    
    def __is_leaf(self, pos):
        return pos > self.size//2 and pos <= self.size

    def __bubble_down(self, pos):
        if self.__is_leaf(pos):
            return
        
        left_child, right_child = self.__left_child(pos), self.__right_child(pos)
        if self.type == 'max':
            if self.heap[pos] < self.heap[left_child] or self.heap[pos] < self.heap[right_child]:
                if self.heap[left_child] > self.heap[right_child]:
                    self.__swap(pos, left_child)
                    self.__bubble_down(left_child)
                else:
                    self.__swap(pos, right_child)
                    self.__bubble_down(right_child)
        else:
            if self.heap[pos] > self.heap[left_child] or self.heap[pos] > self.heap[right_child]:
                if self.heap[left_child] < self.heap[right_child]:
                    self.__swap(pos, left_child)
                    self.__bubble_down(left_child)
                else:
                    self.__swap(pos, right_child)
                    self.__bubble_down(right_child)
    
    def __bubble_up(self, pos):
        if self.type == 'max':
            while self.heap[pos] > self.heap[self.__parent(pos)]:
                self.__swap(pos, self.__parent(pos))
                pos = self.__parent(pos)
        else:
            while self.heap[pos] < self.heap[self.__parent(pos)]:
                self.__swap(pos, self.__parent(pos))
                pos = self.__parent(pos)
      
    def insert(self, value):
        self.size += 1
        self.heap[self.size] = value
        self.__bubble_up(self.size)
    
    def pop(self):
        out = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.__bubble_down(1)

        return out
    
    def top(self):
        return self.heap[1]