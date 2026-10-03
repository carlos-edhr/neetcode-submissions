class MyCircularQueue:

    def __init__(self, k: int):
        self._capacity = k
        # fixed physical storage
        self._buffer: List[int] = [0] * k
        # index of the logical front
        self._front = 0
        # number of stored elements 
        self._size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._buffer[(self._front + self._size) % self._capacity] = value
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._buffer[self._front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._buffer[(self._front + self._size - 1) % self._capacity]
        

    def isEmpty(self) -> bool:
        return self._size == 0
        

    def isFull(self) -> bool:
        return self._size == self._capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()