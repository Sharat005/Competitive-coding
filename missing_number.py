# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortedNums = sorted(nums);
        print(sortedNums);
        n = len(sortedNums);
        
        if(sortedNums[n-1]!=n):
            return n;
        for i in range(n):
            if(i!=sortedNums[i]):
                return i;
