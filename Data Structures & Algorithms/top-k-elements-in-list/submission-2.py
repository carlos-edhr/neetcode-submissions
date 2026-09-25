import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count frequencies in one pass  
        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [num for count, num in heap]





        





















        # freq = Counter(nums)
        # heap = []

        # for num, count in freq.items():
        #     heapq.heappush(heap, (count, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [num for count, num in heap]
      

        