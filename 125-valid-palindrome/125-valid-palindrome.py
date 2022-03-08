class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        updatedStr = ''.join(char for char in s if char.isalnum())
        
        reverse = ""
        for i in range(len(updatedStr)-1, -1, -1):
            reverse += updatedStr[i]
        
        return updatedStr.lower() == reverse.lower()
        
        