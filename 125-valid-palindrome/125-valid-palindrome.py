class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        updatedStr = ''.join(char for char in s if char.isalnum())
        
        if len(updatedStr) < 1:
            return True
        
        start = 0
        end = len(updatedStr) - 1
        
        while start < end:
            if updatedStr[start].lower() != updatedStr[end].lower():
                return False
            start += 1
            end -= 1
            
        return True
        
#         reverse = ""
#         for i in range(len(updatedStr)-1, -1, -1):
#             reverse += updatedStr[i]
        
#         return updatedStr.lower() == reverse.lower()
        
        