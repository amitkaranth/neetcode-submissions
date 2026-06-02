class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # attempt 2; bucket sort
        count = {}
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] = 1+count.get(num, 0)

        for key, freq in count.items():
            bucket[freq].append(key)
        print(bucket)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i] == []:
                continue
            else:
                for num in bucket[i]:
                    res.append(num)
                    k-=1
                if k == 0:
                    break
        return res
