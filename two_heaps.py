"""
Two Heaps

Q: Implement a Median finder,
   where new values are inserted
   into the set, and you have to
   getMedian from that set
"""
import heapq

class Median:
    def __init__(self):
        self.small, self.large = [], []

    def insert(self, num: int) -> None:
        # Push to the max heap and swap with min heap if needed
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Handle uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def getMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        # Even num of elements, return avg of two middle numbers
        return (-1 * self.small[0] + self.large[0]) / 2

