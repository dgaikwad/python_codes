class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map_data = {}
            
        for index, value in enumerate(nums):
            expected_num = target - value
            
            if expected_num in map_data:
                return [map_data[expected_num], index]
            
            map_data[value] = index

# Use below link for better undestanding
# https://www.youtube.com/watch?v=KLlXCFG5TnA
# https://www.code-recipe.com/post/two-sum
