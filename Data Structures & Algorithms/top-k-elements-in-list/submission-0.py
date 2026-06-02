class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = {}
        minHeap = []
        res = []

        # counting all the elements
        for num in nums:
            num_freq[num] = 1+num_freq.get(num, 0)
        # creating a minHeap
        for key, val in num_freq.items():
            heapq.heappush(minHeap, (val, key))
        # storing only the required elements
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        # storing the result in res
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res