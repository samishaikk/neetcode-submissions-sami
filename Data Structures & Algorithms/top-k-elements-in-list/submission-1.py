class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count = Counter(nums)

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # sorted -> returns list of (num, freq) tuples
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
        # We have to take first k elements
        return [num for num, freq in sorted_items[:k]]
