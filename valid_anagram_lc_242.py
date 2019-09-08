
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:      
        dict1 = {}

        if len(s) != len(t):
            return False
        
        for data in range(len(s)):
            if s[data] != t[data]:
                dict1[s[data]] = dict1.get(s[data], 0) +  1
                dict1[t[data]] = dict1.get(t[data], 0) -  1
                
        for data in dict1:
            if dict1[data] != 0:
                return False
        return True
        

# To understand logic : https://www.youtube.com/watch?v=9UtInBqnCgA
