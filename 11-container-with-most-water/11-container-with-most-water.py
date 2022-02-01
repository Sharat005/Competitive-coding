class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        
#         for i in range(len(height)):
#             for j in range(len(height)):
#                 mini = min(height[i], height[j])
#                 maxi = max(maxi, (j-i)*mini)
                
#         return maxi


        maxi = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            mini = min(height[i], height[j])
            maxi = max(maxi, (j-i)* mini)
            if(height[i] > height[j]):
                j -= 1
            else:
                i += 1
            
        return maxi


            