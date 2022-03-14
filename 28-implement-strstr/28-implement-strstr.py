class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if haystack=='' and needle=='':
            return 0
        if haystack=='':
            return -1
        return haystack.find(needle)
#         if len(needle) < 1:
#             return 0
#         if len(needle) > len(haystack):
#             return -1
        
#         i = 0
#         j = 0
#         first = math.inf
        
#         while i < len(haystack) and j < len(needle):
            
#             if haystack[i] == needle[j]:
#                 first = min(first, i)
#                 i += 1
#                 j += 1
#             else:
#                 if j > 0:
#                     j = 0
#                     first = math.inf
#                 i += 1
#             print(first)
            
#             if len(needle) == 1 and j == 1:
#                 return first
#             elif len(needle) != 1 and j == len(needle):
#                 return first
            
        
            
#         return -1
            