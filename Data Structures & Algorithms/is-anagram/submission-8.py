# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         s = sorted(s)
#         t = sorted(t)
#         if s == t:
#             return True
#         return False

class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        counter_s={}
        counter_t={}
        
        for char in s:
            if char not in counter_s:
                counter_s[char] = 1
            else:
                counter_s[char] += 1
        
        for char in t:
            if char not in counter_t:
                counter_t[char] = 1
            else:
                counter_t[char] += 1
        
        if counter_s == counter_t:
            return True
        
        return False

