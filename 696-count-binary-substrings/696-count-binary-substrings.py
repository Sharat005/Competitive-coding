class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
        
#         count = 0
#         output = 0
#         i = 0
#         zeroes = 0
#         ones = 0
        
#         if s[0] == '1':
#             ones = 1
#         else:
#             zeroes = 1
            
#         for j in range(1, len(s)):
#             if s[j] == '0':
#                 zeroes += 1
#             else:
#                 ones += 1
                
#             if s[j] != s[j-1]:
#                 count += 1
                
#             if count > 1:
#                 if zeroes == ones:
#                     output += 1
#                 i += 1
#                 count = 0
                
#         return output
            
        