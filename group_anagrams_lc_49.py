class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        new_dict = defaultdict(list)
        for data in strs:
            count_array = [0] * 26
            for c in data:
                count_array[ord(c) - ord("a")] += 1
            new_dict[tuple(count_array)].append(data)

        return new_dict.values()
        
# https://www.youtube.com/watch?v=vzdNOK2oB2E
