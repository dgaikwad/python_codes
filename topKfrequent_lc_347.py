class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data_dict = dict()
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            data_dict[i] = 1 + data_dict.get(i, 0) 
            
        for n,c in data_dict.items():
            freq[c].append(n)
            
        result  = [] 
        for data in range(len(freq)-1, -1, -1):
            for i in freq[data]:
                result.append(i)
                if k == len(result):
                    return result

# https://www.youtube.com/watch?v=YPTqKIgVk-k
